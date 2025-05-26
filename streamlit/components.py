import streamlit as st
import yaml
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader
import pandas as pd
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/models")
import order as om
import order_list as oml
import user as usr



# def auth_login():
#     with open('.streamlit/auth_config.yaml') as file:
#         config = yaml.load(file, Loader=SafeLoader)

#         # Pre-hashing all plain text passwords once
#         # stauth.Hasher.hash_passwords(config['credentials'])

#         authenticator = stauth.Authenticate(
#             config['credentials'],
#             config['cookie']['name'],
#             config['cookie']['key'],
#             config['cookie']['expiry_days']
#         )
        
#         try:
#             authenticator.login()
#         except Exception as e:
#             st.error(e)
            
#         if st.session_state.get('authentication_status'):
#             authenticator.logout()
#             st.write(f'Welcome *{st.session_state.get("name")}*')
#             st.title('Some content')
#         elif st.session_state.get('authentication_status') is False:
#             st.error('Username/password is incorrect')
#         elif st.session_state.get('authentication_status') is None:
#             st.warning('Please enter your username and password')
            
            
#######################################################################################
######                     Global                                                 #####
#######################################################################################

def display_sidebar():
    with st.sidebar:
        st.page_link("Velostore.py", label="Mes velos")
        st.page_link("pages/2_Velo.py", label="Mon Velo")
        st.page_link("pages/3_Panier.py", label="Mon Panier")
        st.page_link("pages/4_Commandes.py", label="Mes commandes"),
        if 'user' in st.session_state:
            st.page_link("pages/6_Logout.py", label="Se deconnecter"),
            # if st.session_state.user.type == 'admin':
            #     st.page_link("pages/7_Admin.py", label="Ma Page Admin"),
        else:
            st.page_link("pages/5_Login.py", label="Se connecter"),
            
#######################################################################################
#####       Main page : bike brand collection  Velostore.py                       #####
#######################################################################################

def display_all_bikes():
    st.write("Voir tout nos velos")
    bikes = st.session_state.bikes
    for bike_id, bike in bikes.items():
        if "all_bike_brand_select_destination" in st.session_state:
            if st.session_state.all_bike_brand_select_destination == bike["destination"]:
                display_one_bike_brand(bike)
        else: 
            display_one_bike_brand(bike)
    # st.write(st.session_state.bikes)
    

        
def display_one_bike_brand(bike_brand):
    bike = bike_brand
    with st.container(height=600):
        st.title(bike["brand"])
        st.subheader(bike["description"])
        st.text(f"A partir de {bike["price"]}€")
        if 'img' in bike:
            print(f"image :  {bike["img"]}")
            # st.image(f"{st.session_state.img_path}{bike["img"]}")
        st.text(f"Categorie : {bike["destination"]}")
        if st.button("Voir ce velo", key="go_to_bike_page_button_"+str(bike["id"])):
            st.session_state.bike = bike
            st.switch_page("pages/2_Velo.py")

            
def select_box_destination():   
            destinations = st.session_state.destination
            id_destination = [destination[0] for destination in st.session_state.destination]
            st.session_state.all_bike_brand_select_destination = st.selectbox(
                "Choisissez votre type de velo", 
                id_destination, 
                format_func=lambda x: str(destinations[x-1][1]),
                )
            
#######################################################################################
#####                        Bike Page : 2_Velo.py                                #####
#######################################################################################            
            
def display_bike():
    bike = st.session_state.bike
    colors = st.session_state.colors
    sizes = st.session_state.sizes
    st.title(bike["brand"])
    st.subheader(bike["description"])
    st.text(f"A partir de {bike["price"]}€")
    if bike["img"]:
        print(f"image :  {bike["img"]}")
        # st.image(f"{st.session_state.img_path}{bike["img"]}")
    st.text(f"Categorie : {bike["destination"]}")
    # select_color = st.selectbox("Choisissez votre couleur", colors)
    # select_size = st.selectbox("Choisissez votre taille", sizes)
    select_box_colors()
    select_box_sizes()
    # st.session_state.bike_brand = bike_brand
    # st.session_state.bike_color = select_color
    # st.session_state.bike_brand = select_size
    # st.button("Acheter", on_click=add_bike_item_to_cart)
    if st.button("Acheter", key="buy_bike_button"):
        # bike = Bike_item(bike_brand, color, size)
        st.session_state.bike_item = bike
        # add_bike_item_to_cart(bike)
    if st.button("Aller sur votre panier", key="go_to_cart_page_button_"+str(bike["id"])):
        st.switch_page("pages/3_Panier.py")
        
        
def select_box_colors():   
            colors = st.session_state.colors
            id_colors = [color[0] for color in st.session_state.colors]
            st.session_state.bike_brand_select_color = st.selectbox(
                "Choisissez la couleur de votre velo", 
                id_colors, 
                format_func=lambda x: str(colors[x-1][1]),
                )
            
def select_box_sizes():   
            sizes = st.session_state.sizes
            id_sizes = [size[0] for size in st.session_state.sizes]
            st.session_state.bike_brand_select_size  = st.selectbox(
                "Choisissez la couleur de votre velo", 
                id_sizes, 
                format_func=lambda x: str(sizes[x-1][1]),
                )

#######################################################################################
#####                        Cart Page : 3_Panier.py                              #####
####################################################################################### 

def display_order():
    user_id = 1
    order = om.Order(1)
    print(f" order model : {order}")
    # df_order = pd.DataFrame(order)
    # df_order = create_order_dataframe(order)
    st.subheader(f"Votre commande a la date {order["date"]}")
    st.text(f"Cout total de la commande {order["total_price"]}")
    create_order_item_table(order)
    
def create_order_item_table(order):
    products_expander = st.expander("Vos produits")
    products = order["order_item_list"]
    bikes = [item.get("bike") for item in order["order_item_list"]]
    df_bikes = pd.DataFrame(bikes)
    df_bikes = df_bikes.drop(columns="img")
    # df_products = create_order_dataframe(order)
    df_products = pd.DataFrame(products)
    df_order = pd.concat([df_bikes, df_products], axis=1)
    df_order = df_order.drop(columns="bike")
    products_expander.table(df_order)
    # products_expander.table(df_bikes)
    # products_expander.table(df_products)
    return products_expander

def create_order_dataframe(order):
    bikes = [item.get("bike") for item in order["order_item_list"]]
    df_bike = pd.DataFrame(bikes)
    df_order_item = pd.DataFrame(order)
    df_order = pd.concat([df_order_item, df_bike], axis=1)
    df_order = df_order.drop(columns="order_item_list")
    return df_order

#######################################################################################
#####                        Order Page : 4_Commandes.py                          #####
####################################################################################### 

def display_pending_order():
    user_id = st.session_state.user_id
    order = om.get_pending_order(user_id)
    # df_order = pd.DataFrame(order)
    # df_order = create_order_dataframe(order)
    st.subheader(f"Votre panier a la date {order["date"]}")
    st.text(f"Cout total de la commande {order["total_price"]}")
    products_expander = st.expander("Vos produits")
    create_order_item_table(order)
    products_expander.table(create_order_item_table(order))
    
def display_closed_order():
    user_id = st.session_state.user_id
    old_orders = oml.get_closed_order(user_id)
    st.subheader("Vos anciennes commandes")
    st.text("Nombre de commandes passées ")
    create_old_orders_expander(old_orders)
        
    
def create_order_item_table(order):
    products = order["order_item_list"]
    bikes = [item.get("bike") for item in order["order_item_list"]]
    df_bikes = pd.DataFrame(bikes)
    df_bikes = df_bikes.drop(columns="img")
    df_products = pd.DataFrame(products)
    df_order = pd.concat([df_bikes, df_products], axis=1)
    df_order = df_order.drop(columns="bike")
    return df_order

def create_old_orders_expander(orders):
    orders_expander = st.expander("#Vos anciennes commandes")
    for order in orders:
        orders_expander.subheader(f"Date : {order["date"]}")
        orders_expander.text(f"Prix total : {order["total_price"]}")
        create_order_item_table(order)
        orders_expander.table(create_order_item_table(order))
    return orders_expander

#######################################################################################
#####                        Login Page : 5_Login.py                              #####
####################################################################################### 

def display_login_block():
    login =  st.text_input("Login", "Votre login")
    password = st.text_input("Mot de passe", "Password")
    connect = st.button("Se connecter", key="login_button")
    if connect:
        user = usr.User()
        user.login(1)
        if user: 
            st.session_state.user = user
            st.session_state.user_id = 1
            st.write("Je me connecte")
        else:
            st.write("La combinaison login mdp n'est pas la bonne")
    

#######################################################################################
#####                        Logout Page : 6_Logout.py                            #####
#######################################################################################

def display_logout_block():
    logout = st.button("Se deconnecter", key="logout_button")
    if logout:
        del st.session_state.user
        del st.session_state.user_id
        st.write("Je me deconnecte")

#######################################################################################
#####                        Admin page : 7_Admin.py                              #####
#######################################################################################

def create_bike_brand_block():
    creation_brand_expander = st.expander("#Creer un nouveau modele")
    with creation_brand_expander:
        brand = st.text_input("Saisissez le nom de votre modele : ", "brand")
        description = st.text_input("Entrez la description de votre modele", "description")
        price = st.text_input("Entrez le prix de votre modele", "price")
        if st.button("Creer le modele", key="create_bike_button"):
            st.write("Votre modele est créé")       

def main():
    pass

if __name__ == '__main__':
    main()