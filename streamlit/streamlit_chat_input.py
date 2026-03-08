#Example 1: Pin the chat input widget to the bottom of your app
import streamlit as st 


prompt = st.chat_input("Say something")

if prompt:
    st.write(f"User has sent the following prompt: {prompt}")



#Example 3: Let users upload files

st.divider

prompt = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)
if prompt and prompt.text:
    st.markdown(prompt.text)
if prompt and prompt["files"]:
    st.image(prompt["files"][0])


#Example 5: Enable audio recording
import streamlit as st

prompt = st.chat_input(
    "Say or record something",
    accept_audio=True,
)
if prompt and prompt.text:
    st.write("Text:", prompt.text)
if prompt and prompt.audio:
    st.audio(prompt.audio)
    st.write("Audio file:", prompt.audio.name)