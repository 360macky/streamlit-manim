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
openai_key = st.text_input("Write your OpenAI API Key", value="", type="password")
user_wants_code = st.checkbox("Check code generated")

code_input = ""

if user_wants_code:
  is_code_edition_enabled = st.button("Edit code")

  if is_code_edition_enabled:
    code_input = st.text_area("Write your animation idea here", value=code_snippet)
  else:
    st.code(code_snippet, language="python")

class GeneratedScene(Scene):
    def construct(self):
        exec(code_input)


if st.button("Render"):
    GeneratedScene().render()
    st.video("media/videos/1080p60.0/GeneratedScene.mp4")

