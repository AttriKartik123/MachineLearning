'''Add widgets to sidebar
Not only can you add interactivity to your app with widgets, you can organize them into a sidebar. Elements can be passed to st.sidebar using object notation and with notation.'''

# Object notation
import streamlit as st
import time

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")