import streamlit as st
import pandas as pd
import components

st.set_page_config(
    page_title = "Velostore: Votre panier",
    page_icon="🚲"
)

st.write("# Votre Panier 🚲")


def main():
    components.display_sidebar()
    if 'user' in st.session_state:
        components.display_pending_order()
    else:
        components.display_login_block()

if __name__ == '__main__':
    main()