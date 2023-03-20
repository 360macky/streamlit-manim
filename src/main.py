import streamlit as st
from manim import *

st.title("Manim")
st.write("This is a test of Manim in Streamlit")

code_snippet = '''
circle = Circle()
circle.set_fill("#FF0000", opacity=opacity)
self.play(Create(circle))
'''

prompt = st.text_area("Write your animation idea here")
code_input = st.text_area("Write your animation idea here", value=code_snippet)
opacity = st.slider("Choose opacity", min_value=0.0, max_value=1.0, value=0.45)
openai_key = st.text_input("Write your OpenAI API Key", value="", type="password")


st.code(code_snippet, language="python")

class GeneratedScene(Scene):
    def construct(self):
        exec(code_input)


if st.button("Render"):
    GeneratedScene().render()
    st.video("media/videos/1080p60.0/GeneratedScene.mp4")

