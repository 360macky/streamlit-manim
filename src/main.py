import streamlit as st
from manim import *

st.title("Manim")
st.write("This is a test of Manim in Streamlit")

prompt = st.text_area("Write your animation idea here")
color = st.text_input("Give Hex Fill color for circle", value="#FF0000")
opacity = st.slider("Choose opacity", min_value=0.0, max_value=1.0, value=0.45)

code_snippet = '''
    circle = Circle()                   
    circle.set_fill(color, opacity=opacity)
    self.play(Create(circle))
'''

st.code(code_snippet, language="python")

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(color, opacity=opacity)
        self.play(Create(circle))


if st.button("Render"):
    SquareToCircle().render()
    st.video("media/videos/1080p60.0/SquareToCircle.mp4")
