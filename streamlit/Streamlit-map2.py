import streamlit as st
import pandas as pd

file = st.file_uploader("Upload CSV")

if file:
    data = pd.read_csv(file)
    st.map(data)



#
st.title("Location Map Example")

data = pd.DataFrame({
    "lat": [28.6139, 19.0760, 13.0827],
    "lon": [77.2090, 72.8777, 80.2707]
})

st.map(data)