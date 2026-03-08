#Example Without Cache
import streamlit as st
import time


def load_data():
    time.sleep(5)
    return "Data Loaded"

data = load_data()
st.write(data)




#import streamlit as st (((((EXAMPLE WITH CAHCE)))))
st.divider

import time

@st.cache_data
def load_data():
    time.sleep(5)
    return "Data Loaded"

data = load_data()
st.write(data)