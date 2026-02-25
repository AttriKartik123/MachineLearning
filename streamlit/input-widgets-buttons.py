import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")



# add icons to your buttons

left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")


# using keyword shortcuts


with st.container(horizontal=True, horizontal_alignment="distribute"):
    "`A`" if st.button("A", shortcut="A") else "` `"
    "`S`" if st.button("S", shortcut="Ctrl+S") else "` `"
    "`D`" if st.button("D", shortcut="Cmd+Shift+D") else "` `"
    "`F`" if st.button("F", shortcut="Mod+Alt+Shift+F") else "` `"