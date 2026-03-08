#use .update() on the container to change the label, state, or expanded state:
import time
import streamlit as st

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(
        label="Download complete!", state="complete", expanded=False
    )

st.button("Rerun")


#manual status control 


status = st.status("Starting process...")

time.sleep(2)
status.write("Downloading data...")

time.sleep(2)
status.write("Processing data...")

time.sleep(2)
status.update(label="Process completed", state="complete")