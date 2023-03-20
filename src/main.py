import streamlit as st
from manim import *

st.title("Manim")
st.write("This is a test of Manim in Streamlit")

code_snippet = '''
circle = Circle()
circle.set_fill("#FF0000", opacity=0.5)
self.play(Create(circle))
'''

prompt = st.text_area("Write your animation idea here")
code_input = st.text_area("Write your animation idea here", value=code_snippet)
openai_key = st.text_input("Write your OpenAI API Key", value="", type="password")


# st.code(code_snippet, language="python")

class GeneratedScene(Scene):
    def construct(self):
        exec(code_input)


if st.button("Render", type="primary"):
    GeneratedScene().render()
    st.video("media/videos/1080p60.0/GeneratedScene.mp4")

