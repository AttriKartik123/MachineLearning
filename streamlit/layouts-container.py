#Example 1: Inserting elements using ``with`` notation
import streamlit as st

st.title("Simple Container Example")

# Create a container
my_container = st.container()

# Add content inside the container
with my_container:
    st.header("This is inside the container")
    st.write("You can group multiple elements here.")
    st.button("Click Me")

st.write("This is outside the container.")

st.divider()








#Example 3: Grid layout with columns and containers
import streamlit as st

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")

st.divider()





#Example 4: Vertically scrolling container
import streamlit as st

long_text = "Lorem ipsum. " * 1000

with st.container(height=300):
    st.markdown(long_text)

st.divider()






#Example 5: Horizontal container
import streamlit as st

flex = st.container(horizontal=True, horizontal_alignment="right")

for card in range(3):
    flex.button(f"Button {card + 1}")

    st.divider()


    