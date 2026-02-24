import streamlit as st
st.header("Welcome")
st.title("Kartik Attri")
st.subheader("Student")

st.success("Winner")
st.info("Get Details")
st.warning("Try again")
st.error("Loser")
err=ValueError("FIND IT")
st.exception(err)

st.write(range(20))

# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    # Show this text only when the checkbox is checked
    st.text("Showing the widget")

status = st.radio("Select Gender:", ['Male', 'Female','Non Binary'])

# Display the selected option using success message
if status == 'Male':
    st.success("Male")
elif status == 'Female':
    st.success("Female")