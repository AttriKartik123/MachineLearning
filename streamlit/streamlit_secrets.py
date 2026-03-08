import streamlit as st 

user= st.secrets["database"]["user"]
password = st.secrets["database"]["password"]

st.write("Database User:" , user)