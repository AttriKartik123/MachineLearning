import streamlit as st
import pandas as pd

file = st.file_uploader("Upload CSV")

if file:
    data = pd.read_csv(file)
    st.map(data)