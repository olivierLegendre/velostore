import streamlit as st
import pandas as pd
import components

st.set_page_config(
    page_title = "Velostore: Vos commandes",
    page_icon="🚲"
)

st.write("# Vos Commandes 🚲")

def main():
    components.display_sidebar()
    components.display_closed_order()

if __name__ == '__main__':
    main()