import streamlit as st
from password_generator import show_password_generator
from password_test import show_password_test

#-------page config----------
st.set_page_config(
    page_title="🔐 Smart Password Suite",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Smart Password Suite")
st.markdown("Securely generate and check for password's validity and strength - both in one place!")
st.markdown("---")


#-------header navigation----------
tabs = st.tabs(["🔑 Password generator", "💪 Password strength test"])

with tabs[0]:
    show_password_generator()

with tabs[1]:
    show_password_test()

#--------footer------
st.markdown("---")
st.caption("🔐 Made with ❤ using streamlit")