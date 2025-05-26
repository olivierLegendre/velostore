import streamlit as st
import os, sys
import components
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/models")
# import bike_brand as bb
import bike_brand_list as bbl
import internal_parameters_list as ipl
from typing import Dict, Any

st.set_page_config(
    page_title = "Velostore: Nos velos",
    page_icon="🚲"
)

st.write("# Bienvenue chez VeloStore! 👋")

def set_parameters() -> None:
    """
    Initialise les paramètres internes dans l'état de la session Streamlit.
    """
    if 'img_path' not in st.session_state:
        st.session_state.img_path = "streamlit/static/"
        pass
    parameters = ipl.InternalParametersList()
    if 'colors' not in st.session_state:
        colors = parameters.get_bike_color_list()
        # print(f"colors : {colors}")
        st.session_state.colors = colors
    if 'sizes' not in st.session_state:
        sizes = parameters.get_bike_size_list()
        # print(f"sizes : {sizes}")
        st.session_state.size = sizes
    if 'destinations' not in st.session_state:
        destinations = parameters.get_bike_destination_list()
        # print(f"destinations : {destinations}")
        st.session_state.destination = destinations

def set_datas_to_session() -> None:
    """
    Initialise les données des vélos dans l'état de la session Streamlit.
    """
    if 'bikes' not in st.session_state:
        st.session_state.bikes = get_all_bikes()
    #bikes
    #prices
    #brand
    #destinations
    pass
    
# @st.cache_data
def get_all_bikes() -> Dict[str, Any]:
    """
    Récupère la liste de tous les vélos disponibles.

    Returns:
        Dict[str, Any]: Dictionnaire contenant la liste des vélos.
    """
    bikes = bbl.BikeBrandList()
    all_bikes = bikes.get_bike_brand_list()
    print(f"liste des velos : {all_bikes}")
    return all_bikes
    
def get_all_brand() -> None:
    """
    Récupère toutes les marques de vélos. (À implémenter)
    """
    pass
def get_all_destinations() -> None:
    """
    Récupère toutes les destinations de vélos. (À implémenter)
    """
    pass

def main() -> None:
    """
    Fonction principale pour exécuter l'application.
    """
    set_parameters()
    set_datas_to_session()
    components.display_sidebar()
    components.display_all_bikes()
    # components.bike_display()

if __name__ == '__main__':
    main()