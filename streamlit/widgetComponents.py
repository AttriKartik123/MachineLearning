import streamlit as st 


#Audio
#st.audio("abxx.mp3" , format="audio/mpeg" , loop=True)


#Audio Input
st.audio_input("Speak")
st.divider()


#Badges
st.badge("New")
st.badge("Success", color="red")

st.balloons()
st.divider()


st.camera_input("Click Me")
st.divider()

st.caption("Hello guys this is caption ")

st.code( """
    print("Helo world") 
""", language="python")


st.color_picker("Pick")
st.divider()


st.download_button("Download btn" , data=" lorem ipsum")
st.divider()



#st.help("print")
st.divider()



#image
# st.image(abc.png ,format= "img/png")

st.snow()


#latex
st.latex("a^3 + b^6")


st.slider("slide it:")

