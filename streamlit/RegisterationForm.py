'''import streamlit as st

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

    '''
import streamlit as st

st.title("Registration Form")

with st.form("registration_form"):

    c1, c2 = st.columns([1, 3])
    username = c2.text_input("Username:", label_visibility="collapsed")
    c1.text("Username")

    c3, c4 = st.columns([1, 3])
    password = c4.text_input("Password:", type="password", label_visibility="collapsed")
    c3.text("Password")

    c5, c6 = st.columns([1, 3])
    repassword = c6.text_input("Retype Password:", type="password", label_visibility="collapsed")
    c5.text("Retype Password")

    c7, c8 = st.columns([1, 3])
    gender = c8.radio("Select Gender:", ["Male", "Female", "Trans"], horizontal=True, label_visibility="collapsed")
    c7.text("Gender")

    c9, c10 = st.columns([1, 3])
    correspondance = c10.text_area("Correspondence", label_visibility="collapsed")
    c9.text("Correspondence")

    c11, c12 = st.columns([1, 3])
    mobileNumber = c12.text_input("Mobile Number:", label_visibility="collapsed")
    c11.text("Mobile Number")

    c13, c14 = st.columns([1, 3])
    PinCode = c14.text_input("Pincode:", label_visibility="collapsed")
    c13.text("Pincode")

    c15, c16 = st.columns([1, 3])
    options = ["Singing", "Dancing", "Drawing", "Bathing"]
    Interests = c16.pills("Interests", options, selection_mode="multi", label_visibility="collapsed")
    c15.text("Interests")

    c17, c18 = st.columns([1, 3])
    dob = c18.date_input("Date of Birth:", label_visibility="collapsed")
    c17.text("Date of Birth")

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