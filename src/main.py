from manim.mobject.geometry import Circle
from manim.animation.creation import Create
from manim.scene.scene import Scene
from manim.utils.color import Colors
import streamlit as st

st.title("Manim")
st.write("This is a test of Manim in Streamlit")

prompt = st.textarea("Write your animation idea here")
color = st.text_input("Give Hex Fill color for circle", value=Colors.blue_e.value)
opacity = st.slider("Choose opacity", min_value=0.0, max_value=1.0, value=0.45)

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()                   
        circle.set_fill(color, opacity=opacity)
        self.play(Create(circle))

if st.button("Render"):
    SquareToCircle().render()
    # Show /app/streamlit-manim/media/videos/1080p60.0/SquareToCircle.mp4
    st.video("media/videos/1080p60.0/SquareToCircle.mp4")

# SquareToCircle().render()

# Show a ls of all the available files

# st.video('/app/media/videos/1080p60.0/SquareToCircle.mp4')

