import streamlit as st
from manim import *

st.title("Manim")
st.write("This is a test of Manim in Streamlit")

prompt = st.text_area("Write your animation idea here")
opacity = st.slider("Choose opacity", min_value=0.0, max_value=1.0, value=0.45)

code_snippet = '''
def construct(self):
    circle = Circle()
    circle.set_fill("#FF0000", opacity=opacity)
    self.play(Create(circle))
'''

st.code(code_snippet, language="python")

class GeneratedScene(Scene):
    eval(code_snippet)


if st.button("Render"):
    GeneratedScene().render()
    st.video("media/videos/1080p60.0/GeneratedScene.mp4")

