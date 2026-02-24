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

st.badge("Home", color="blue")


st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")


st.divider()

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)


#widgets
#1 button
import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")



#download button

message = st.text_area("Message", value="Lorem ipsum.\nStreamlit is cool.")

if st.button("Prepare download"):
    st.download_button(
        label="Download text",
        data=message,
        file_name="message.txt",
        on_click="ignore",
        type="primary",
        icon=":material/download:",
    )



    