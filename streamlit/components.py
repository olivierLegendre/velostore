import streamlit as st
import yaml
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader
from typing import Dict, Any



def auth_login() -> None:
    """
    Gère l'authentification de l'utilisateur en utilisant un fichier de configuration YAML.
    Affiche un message de bienvenue si l'authentification est réussie, sinon affiche une erreur.
    """
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
            

        

def display_bike(bike_brand: Dict[str, Any]) -> None:
    """
    Affiche les détails d'un vélo spécifique.

    Args:
        bike_brand (Dict[str, Any]): Dictionnaire contenant les détails du vélo.
    """
    bike = bike_brand
    colors = st.session_state.colors
    size = st.session_state.size
    st.title(bike["brand"])
    st.subheader(bike["description"])
    st.text(f"A partir de {bike["price"]}€")
    st.image(f"{st.session_state.img_path}{bike["image"]}")
    st.text(f"Categorie : {bike["destination"]}")
    select_color = st.selectbox("Choisissez votre couleur", colors)
    select_size = st.selectbox("Choisissez votre taille", size)
    st.session_state.bike_brand = bike_brand
    st.session_state.bike_color = select_color
    st.session_state.bike_brand = select_size
    # st.button("Acheter", on_click=add_bike_item_to_cart)
    if st.button("Acheter"):
        # bike = Bike_item(bike_brand, color, size)
        st.session_state.bike_item = bike
        # add_bike_item_to_cart(bike)
    if st.button("Aller sur votre panier"):
        st.switch_page("pages/3_Panier.py")
        
def display_one_bike_brand(bike_brand: Dict[str, Any]) -> None:
    """
    Affiche les détails d'une marque de vélo spécifique.

    Args:
        bike_brand (Dict[str, Any]): Dictionnaire contenant les détails de la marque de vélo.
    """
    bike = bike_brand
    print(f"bike : {bike}")
    st.title(bike["brand"])
    st.subheader(bike["description"])
    st.text(f"A partir de {bike["price"]}€")
    if 'image' in bike:
        st.image(f"{st.session_state.img_path}{bike["image"]}")
    st.text(f"Categorie : {bike["destination"]}")

def display_all_bikes() -> None:
    """Affiche tous les vélos disponibles."""
    st.write("Je vais afficher tous les velos")
    bikes = st.session_state.bikes
    for bike_id, bike in bikes.items():
        print(f" bike unique : {bike}")
        display_one_bike_brand(bike)
    # st.write(st.session_state.bikes)
    
def display_sidebar() -> None:
    """Affiche la barre latérale avec des liens vers différentes pages."""
    with st.sidebar:
        st.page_link("Velostore.py", label="Mes velos")
        st.page_link("pages/2_Velo.py", label="Mon Velo")
        st.page_link("pages/3_Panier.py", label="Mon Panier")
        st.page_link("pages/4_Commandes.py", label="Mes commandes"),
        st.page_link("pages/5_Login.py", label="Se connecter"),
        
        st.page_link("pages/6_Logout.py", label="Se deconnecter"),
        st.page_link("pages/7_Admin.py", label="Ma Page Admin"),

def display_login_block() -> None:
    """Affiche un bloc de déconnexion pour l'utilisateur."""
    login =  st.text_input("Login", "Votre login")
    password = st.text_input("Mot de passe", "Password")
    connect = st.button("Se connecter")
    if connect:
        st.write("Je me connecte")
    

def display_logout_block() -> None:
    """Affiche un bloc de déconnexion pour l'utilisateur."""
    logout = st.button("Se deconnecter")
    if logout:
        st.write("Je me deconnecte")
        
def create_bike_brand_block() -> None:
    """Affiche un bloc pour créer une nouvelle marque de vélo."""
    creation_brand_expander = st.expander("#Creer un nouveau modele")
    with creation_brand_expander:
        brand = st.text_input("Saisissez le nom de votre modele : ", "brand")
        description = st.text_input("Entrez la description de votre modele", "description")
        price = st.text_input("Entrez le prix de votre modele", "price")
        create_bike_brand = st.button("Creer le modele")
        if create_bike_brand:
            st.write("Votre modele est créé")

def main():
    """Fonction principale pour exécuter l'application."""
    pass

if __name__ == '__main__':
    main()