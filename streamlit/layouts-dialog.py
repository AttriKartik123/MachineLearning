import streamlit as st

st.title("Streamlit Dialog Example")

# Define a dialog
@st.dialog("My Dialog")
def show_dialog():
    st.write("This is a dialog window.")
    name = st.text_input("Enter your name")
    
    if st.button("Submit"):
        st.success(f"Hello, {name}!")
        st.rerun()

# Button to open dialog
if st.button("Open Dialog"):
    show_dialog()