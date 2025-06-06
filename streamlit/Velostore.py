import streamlit as st
import os, sys
import components
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/models")
# import bike_brand as bb
import bike_brand_list as bbl
import internal_parameters_list as ipl

st.set_page_config(
    page_title = "Velostore: Nos velos",
    layout="wide",
    page_icon="🚲",
)

st.write("# Bienvenue chez VeloStore! 👋")

def set_parameters():
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
        st.session_state.sizes = sizes
        st.session_state.sizes = sizes
    if 'destinations' not in st.session_state:
        destinations = parameters.get_bike_destination_list()
        # print(f"destinations : {destinations}")
        st.session_state.destination = destinations

def set_datas_to_session():
    if 'bikes' not in st.session_state:
        st.session_state.bikes = get_all_bikes()
    pass

def get_all_bikes():
    bikes = bbl.BikeBrandList('mongodb')
    bikes = bikes.get_bike_brand_object_list()
    return bikes

def main():
    set_parameters()
    set_datas_to_session()
    components.display_sidebar()
    col1, col2 = st.columns(2)
    with col1:
        
        components.display_all_bikes()
    with col2:
        components.select_box_destination()

if __name__ == '__main__':
    main()