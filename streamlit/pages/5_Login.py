import streamlit as st
import components
import streamlit_authenticator as stauth

def main():
    components.display_sidebar()
    # components.display_login_block()
    # components.auth_login()
    components.display_login_block()
    pass

if __name__ == '__main__':
    main()