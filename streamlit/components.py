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

#######################################################################################
######                     Global                                                 #####
#######################################################################################

def display_sidebar():
    """dispaly sidebar
        with somes pages dynamicaly called
    """
    with st.sidebar:
        st.page_link("Velostore.py", label="Mes velos")
        st.page_link("pages/2_Velo.py", label="Mon Velo")
        if 'user' in st.session_state:
            st.page_link("pages/3_Panier.py", label="Mon Panier")
            st.page_link("pages/4_Commandes.py", label="Mes commandes"),
            st.page_link("pages/6_Logout.py", label="Se deconnecter"),
            # if st.session_state.user.type == 'admin':
            #     st.page_link("pages/7_Admin.py", label="Ma Page Admin"),
        else:
            st.page_link("pages/5_Login.py", label="Se connecter"),
            
#######################################################################################
#####       Main page : bike brand collection  Velostore.py                       #####
#######################################################################################

def display_all_bikes():
    """retrieve all the bike brand available
    """
    st.write("Voir tout nos velos")
    bikes = st.session_state.bikes
    for bike_id, bike in bikes.items():
        if "all_bike_brand_select_destination" in st.session_state:
            session_destination = st.session_state.all_bike_brand_select_destination
            if session_destination == bike.destination:
                display_one_bike_brand(bike)
        else:
            display_one_bike_brand(bike)
    

        
# def display_one_bike_brand(bike_brand: object):
#     """Dispaly the selected bike brand
#         Old version
#     Args:
#         bike_brand (object): the bike brand to display
#     """
#     bike = bike_brand
#     with st.container(height=800):
#         st.title(bike["brand"])
#         st.subheader(bike["description"])
#         st.text(f"A partir de {bike["price"]}€")
#         if 'img' in bike:
#             st.image(f"{st.session_state.img_path}{bike["img"]}")
#         st.text(f"Categorie : {bike["destination"]}")
#         if st.button("Voir ce velo", key="go_to_bike_page_button_"+str(bike["id"])):
#             st.session_state.bike = bike
#             st.switch_page("pages/2_Velo.py")
            
def display_one_bike_brand(bike_brand: object):
    """Dispaly the selected bike brand

    Args:
        bike_brand (object): the bike brand to display
    """
    bike = bike_brand
    with st.container(height=800):
        st.title(bike.brand)
        st.subheader(bike.description)
        st.text(f"A partir de {bike.price}€")
        if bike.img is not None:
            st.image(f"{st.session_state.img_path}{bike.img}")
        st.text(f"Categorie : {bike.destination}")
        if st.button("Voir ce velo", key="go_to_bike_page_button_"+str(bike.id)):
            st.session_state.bike = bike
            st.switch_page("pages/2_Velo.py")

            
def select_box_destination():
    """Create a selecbox with all the destination
    """
    destinations = st.session_state.destination
    value_destination = [destination[1] for destination in destinations]
    st.session_state.all_bike_brand_select_destination = st.selectbox(
        "Choisissez votre type de velo",
        value_destination,
    )
            
#######################################################################################
#####                        Bike Page : 2_Velo.py                                #####
#######################################################################################            
            
def display_bike():
    """display a single bike, customizable on size and color
        and Acheter et aller sur votre panier buttons
    """
    if 'bikes' not in st.session_state:
        st.error("Aucun vélo sélectionné.")
        return
    bike = st.session_state.bike
    st.title(bike.brand)
    st.subheader(bike.description)
    st.text(f"A partir de {bike.price}€")
    if bike.img:
        st.image(f"{st.session_state.img_path}{bike.img}")
    st.text(f"Categorie : {bike.destination}")
    select_box_colors()
    select_box_sizes()
    if st.button("Acheter", key="buy_bike_button"):
        if 'user' in st.session_state:
            order = om.Order()
            brand_id = bike.id
            id_user = st.session_state.user_id
            color = st.session_state.bike_brand_select_color
            size = st.session_state.bike_brand_select_size
            order_id = order.place_order_with_bike(id_user, brand_id, size, color, bike.price)
            st.session_state.order_id = order_id
        else:
            st.switch_page("pages/5_Login.py")
    if st.button("Aller sur votre panier", key="go_to_cart_page_button_"+str(bike.id)):
        st.switch_page("pages/3_Panier.py")
        
        
def select_box_colors():
    """create a selectbox with all the colors
    """
    colors = st.session_state.colors
    id_colors = [color[0] for color in st.session_state.colors]
    
    st.session_state.bike_brand_select_color = st.selectbox(
        "Choisissez la couleur de votre velo", 
        id_colors, 
        format_func=lambda x: str(colors[x-1][1]),
        )
            
def select_box_sizes():
    """create a selectbox with all the sizes
    """
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

def display_pending_order():
    """display the ongoing order and offer to pay for it, or go to the cart"""
    user_id = st.session_state.user_id
    order_list_model = oml.OrderList()
    order_dict = order_list_model.get_pending_order_by_user(user_id)
    if len(order_dict):
        order_id = next(iter(order_dict))
        order = order_dict[order_id]
        st.subheader(f"Votre commande a la date {order["date"]}")
        st.text(f"Cout total de la commande {order["total_price"]}")
        create_order_item_table_cart(order)
        if st.button("Payer"):
            pay(order_id)
    else:
        st.write("Pas de commande pour le moment")
        if st.button("Voir Nos Velos "):
            st.switch_page("Velostore.py")
    
def create_order_item_table_cart(order: object):
    """
    create a streamlit table with the order items
    """
    products_expander = st.expander("Vos produits")
    df_bikes = create_order_dataframe(order)
    products_expander.table(df_bikes)
    return products_expander

def pay(order_id: int):
    """Pass the order to payé"""
    order_model = om.Order()
    if order_model.pay_order(order_id) == 1:
        st.switch_page("pages/4_Commandes.py")
    else:
        print("something is wrong with the payment")
    

def create_order_dataframe(order: object):
    """create the dataframe used by the table """
    order_id = order["id_order"]
    order_model = om.Order()
    order_item = order_model.get_order_item_by_id_order(order_id)
    st.write(order_item)
    products = order_item
    key_to_keep = ['id_order', 'brand', 'size', 'color', 'nb_unit', 'total_price']
    order_item_list = [value_order_item for value_order_item in products.values()]
    bikes = list()
    for order_item in order_item_list:
        bikes.append({key:value for (key,value) in order_item.items() if key in key_to_keep})
    df_bikes = pd.DataFrame(bikes)
    return df_bikes

#######################################################################################
#####                        Order Page : 4_Commandes.py                          #####
####################################################################################### 

def display_closed_order():
    """display the orders already payed"""
    user_id = st.session_state.user_id
    order_list = oml.OrderList()
    old_orders = order_list.get_closed_order_by_user(user_id)
    st.subheader("Vos anciennes commandes")
    st.text(f"Nombre de commandes passées : {len(old_orders)}")
    create_old_orders_expander(old_orders)
        
    
def create_order_item_table(order: object):
    """create a streamlit table with the order item"""
    products = order["order_item_list"]
    bikes = [item.get("bike") for item in order["order_item_list"]]
    df_bikes = pd.DataFrame(bikes)
    df_bikes = df_bikes.drop(columns="img")
    df_products = pd.DataFrame(products)
    df_order = pd.concat([df_bikes, df_products], axis=1)
    df_order = df_order.drop(columns="bike")
    return df_order

def create_old_orders_expander(orders):
    """add the table to a expander"""
    orders_expander = st.expander("#Vos anciennes commandes")
    for order in orders.values():
        orders_expander.subheader(f"Date : {order["date"]}")
        orders_expander.text(f"Prix total : {order["total_price"]}")
        orders_expander.table(create_order_dataframe(order))
    return orders_expander

#######################################################################################
#####                        Login Page : 5_Login.py                              #####
####################################################################################### 

def display_login_block():
    """create a login form"""
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

#######################################################################################
#####                        Logout Page : 6_Logout.py                            #####
#######################################################################################

def display_logout_block():
    """create a logout form"""
    logout = st.button("Se deconnecter", key="logout_button")
    if logout:
        del st.session_state.user
        del st.session_state.user_id
        st.write("Je me deconnecte")

#######################################################################################
#####                        Admin page : 7_Admin.py                              #####
#######################################################################################


#######################################################################################
#####                        Admin page : 7_Admin.py                              #####
#######################################################################################

def create_bike_brand_block():
    """not implemented yet"""
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