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

prompt = st.text_area("Write your animation idea here", "Draw a blue circle")
openai_api_key = st.text_input(
    "Write your OpenAI API Key", value="", type="password")
code_input = st.text_area("Write your animation idea here", value=code_snippet)

if st.button("Generate animation", type="primary"):

    openai.api_key = openai_api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You write only Manim scripts for animations in Python. Generate code, not text. Do not explain code. Do not use other library than Manim. At the end use 'self.play'"},
                {"role": "user", "content": f"Animation Request: {prompt}"}],
        max_tokens=200
    )

    code_response = response.choices[0].message.content

    logger.info(f"Code response: {code_response}")

    class GeneratedScene(Scene):
        def construct(self):
            exec(code_input)
    GeneratedScene().render()
    st.video("media/videos/1080p60.0/GeneratedScene.mp4")
