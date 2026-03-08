#charts elements :
#Here are some simple examples of charts in Streamlit. Streamlit can quickly display charts using built-in functions or popular libraries like Matplotlib, Plotly, and Altair.

import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart Example")

st.write("This example shows how to create a simple line chart in Streamlit using random data.")

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.subheader("Generated Data")
st.write(data)

st.subheader("Line Chart")
st.line_chart(data)

#------------------------------------------------->

st.title("Line Chart example 2")
data = {
    "Day": ["Mon", "Tue", "Wed" , "Thu" , "Fri"] ,
    "Sales": [100 ,150 ,120 ,180 , 200]
}

df= pd.DataFrame(data)
df = df.set_index("Day")

st.line_chart(df)

#---------------------------------------------------------------------------->
#BAR CHART

st.divider()
st.title("Bar Chart example 1")
#example 1 - simple bar charts
import streamlit as st
import pandas as pd

data = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Sales": [30, 50, 20]
})

data = data.set_index("Product")

st.bar_chart(data)

#------------------------------------------------------------>
st.divider()
st.title("Area chart example")

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.area_chart(data)

#------------------------------------------------------------------->
st.divider()
st.title("Area chart example2")

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Visitors": [200, 300, 250, 400, 350]
}

df = pd.DataFrame(data)
df = df.set_index("Day")

st.area_chart(df)    
