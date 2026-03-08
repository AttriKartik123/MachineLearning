#Example with Real City Data

import streamlit as st
import pandas as pd

data = pd.DataFrame({
    "city": ["New York", "London", "Tokyo"],
    "lat": [40.7128, 51.5074, 35.6762],
    "lon": [-74.0060, -0.1278, 139.6503]
})

st.map(data)