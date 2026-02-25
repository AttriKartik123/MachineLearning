import streamlit as st

st.title("Registration Form")

with st.form("registration_form"):
    
    username = st.text_input("Username:")
    
    password = st.text_input("Password:", type="password")
    repassword = st.text_input("Retype Password:", type="password")

    gender = st.radio(
        "Select Gender:",
        ["Male", "Female", "Trans"]
    )

    correspondance = st.text_area("Correspondence")

    mobileNumber = st.text_input("Mobile Number:")
    PinCode = st.text_input("Pincode:")

    options = ["Singing", "Dancing", "Drawing", "Bathing"]
    Interests = st.pills("Interests", options ,selection_mode="multi")

    dob = st.date_input("Date of Birth:")

    submitted = st.form_submit_button("Submit")


if submitted:
    st.success("Form Submitted Successfully!")

    st.write("Submitted Details")
    st.write("Username:", username)
    st.write("Gender:", gender)
    st.write("Correspondence:", correspondance)
    st.write("Mobile Number:", mobileNumber)
    st.write("Pincode:", PinCode)
    st.write("Interests:", ", ".join(Interests))
    st.write("Date of Birth:", dob)

    