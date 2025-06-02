import streamlit as st
import components

st.set_page_config(
    page_title = "Velostore: Votre velo",
    page_icon="🚲"
)

st.write("# Choisissez votre Velo 🚲")


def main():
    components.display_sidebar()
    if 'bike' not in st.session_state:
        st.error("Aucun vélo sélectionné.")
        return
    components.display_bike()
    pass

if __name__ == '__main__':
    main()