import streamlit as st
from numpy.random import default_rng

st.title("Streamlit Tabs Examples")

# ---------------------------
# Example 1: Context manager
# ---------------------------
st.header("Example 1: Use context management")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.subheader("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.subheader("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.subheader("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


# ---------------------------
# Example 2: Call methods directly
# ---------------------------
'''
st.header("Example 2: Call methods directly")

rng = default_rng(0)
df = rng.standard_normal((10, 1))

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

tab1.subheader("A tab with a chart")
tab1.line_chart(df)

tab2.subheader("A tab with the data")
tab2.write(df)
'''

# ---------------------------
# Example 3: Styled labels
# ---------------------------
st.header("Example 3: Styled tab labels")

# NOTE: Remove `default=` if you get an error (older Streamlit versions)
tab1, tab2, tab3 = st.tabs(
    [":cat: Cat", ":dog: Dog", ":rainbow[Owl]"]
)

with tab1:
    st.subheader("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.subheader("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.subheader("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)