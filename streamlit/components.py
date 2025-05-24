import streamlit as st
import yaml
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader



def auth_login():
    with open('.streamlit/auth_config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

        # Pre-hashing all plain text passwords once
        # stauth.Hasher.hash_passwords(config['credentials'])

        authenticator = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days']
        )
        
        try:
            authenticator.login()
        except Exception as e:
            st.error(e)
            
        if st.session_state.get('authentication_status'):
            authenticator.logout()
            st.write(f'Welcome *{st.session_state.get("name")}*')
            st.title('Some content')
        elif st.session_state.get('authentication_status') is False:
            st.error('Username/password is incorrect')
        elif st.session_state.get('authentication_status') is None:
            st.warning('Please enter your username and password')
            

        



#######################################################################################
######                     Global                                                 #####
#######################################################################################

def display_sidebar():
    with st.sidebar:
        st.page_link("Velostore.py", label="Mes velos")
        st.page_link("pages/2_Velo.py", label="Mon Velo")
        st.page_link("pages/3_Panier.py", label="Mon Panier")
        st.page_link("pages/4_Commandes.py", label="Mes commandes"),
        st.page_link("pages/5_Login.py", label="Se connecter"),
        
        st.page_link("pages/6_Logout.py", label="Se deconnecter"),
        st.page_link("pages/7_Admin.py", label="Ma Page Admin"),

def display_login_block():
    login =  st.text_input("Login", "Votre login")
    password = st.text_input("Mot de passe", "Password")
    connect = st.button("Se connecter", key="login_button")
    if connect:
        st.write("Je me connecte")
    

def display_logout_block():
    logout = st.button("Se deconnecter", key="logout_button")
    if logout:
        st.write("Je me deconnecte")
        
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

#######################################################################################
#####                        Order Page : 4_Panier.py                             #####
####################################################################################### 

#######################################################################################
#####                        Login Page : 5_Login.py                              #####
####################################################################################### 

#######################################################################################
#####                        Logout Page : 6_Logout.py                            #####
#######################################################################################

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