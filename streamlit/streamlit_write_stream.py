import streamlit as st
import time

def message():
    yield "Hello "
    time.sleep(1)
    
    yield "How "
    time.sleep(1)
    
    yield "are "
    time.sleep(1)
    
    yield "you?"

st.write_stream(message)


st.divider()




#---------------------
import streamlit as st
import time

prompt = st.chat_input("Ask something")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        def bot_reply():
            text = "This response is streaming like ChatGPT."
            for word in text.split():
                yield word + " "
                time.sleep(0.3)

        st.write_stream(bot_reply)