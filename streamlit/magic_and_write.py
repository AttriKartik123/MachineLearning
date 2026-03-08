import streamlit as st
import pandas as pd

st.title("Streamlit Magic vs Write Example")

# Using st.write()
name = "Rahul"
age = 22

st.write("Name:", name)
st.write("Age:", age)

# Using Magic (no st.write needed)
city = "Delhi"
city

# Data example
data = pd.DataFrame({
    "Student": ["Aman", "Riya", "Karan"],
    "Marks": [85, 90, 78]
})

# Magic display
data

# st.write display
st.write("Student Data Table:")
st.write(data)