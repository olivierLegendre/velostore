import streamlit as st
import components

st.set_page_config(
    page_title = "Velostore: Votre velo",
    page_icon="🚲"
)

st.write("# Choisissez votre Velo 🚲")

img_path = "streamlit/static/"

def get_one_bike():
    bike = dict()
    bike["brand"] = "rockrider"
    bike["description"] = "Oh, le joli velo"
    bike["price"] = 150
    bike["image"] = "A30M.jpg"
    bike["destination"] = "vtt"
    return bike
    

bike = get_one_bike()

def add_bike_item_to_cart():
    # bike_brand = st.session_state.bike_brand
    # color = st.session_state.bike_color
    # size = st.session_state.bike_brand
    # bike = Bike_item(bike_brand, color, size)
    st.session_state.bike_item = bike

def bike_display(bike_brand):
    bike = bike_brand
    colors = list(["bleu", "rouge", "vert", "jaune", "orange"])
    size = list(["S", "M", "L", "XL"])
    st.title(bike["brand"])
    st.subheader(bike["description"])
    st.text(f"A partir de {bike["price"]}€")
    st.image(f"{img_path}{bike["image"]}")
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
        add_bike_item_to_cart(bike)
    if st.button("Aller sur votre panier"):
        st.switch_page("pages/3_Panier.py")
    
bike_display(bike)


def main():
    components.display_sidebar()
    pass

if __name__ == '__main__':
    main()