import streamlit as st
import openai
from manim import *

st.title("Manim")
st.write("This is a test of Manim in Streamlit")

code_snippet = '''
circle = Circle()
circle.set_fill("#FF0000", opacity=0.5)
self.play(Create(circle))
'''

prompt = st.text_area("Write your animation idea here")
openai.api_key = st.text_input(
    "Write your OpenAI API Key", value="", type="password")
code_input = st.text_area("Write your animation idea here", value=code_snippet)

if st.button("Generate animation", type="primary"):

    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=[{"role": "system", "content": "You will write Manim script for animations in Python. Generate code, not text. Do not use any other library. Do not explain. At the end use 'self.play'."},
                {"role": "user", "content": f"Request Manim animation of: {prompt}."}],
    )

    code_response = response["choices"][0]["text"]

    logger.info(f"Code response: {code_response}")

    class GeneratedScene(Scene):
        def construct(self):
            exec(code_input)
    GeneratedScene().render()
    st.video("media/videos/1080p60.0/GeneratedScene.mp4")
