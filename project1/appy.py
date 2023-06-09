import os
from APIkey import apikey

import streamlit as st
from langchain.llms import OpenAI



os.environ['OPENAI_API_KEY'] = apikey

llm = OpenAI(temperature=0.6)

st.set_page_config(
    page_title="Icon Generator",
    page_icon="🖌️",
)

st.title("App Logo Idea Generator")
st.caption("Are you developing an app or need a logo for your brand? Getting started too daunting? Use this tool to as a starting point and roadmap to creating the perfect representation of your brand!")
#spacing
st.write("")

#input elements
st.write('**What is the app called?**')
nameInput = st.text_input(':green[ex: *Instragram*]')
st.write("")
st.write('**What is the purpose of the app?**')
purposeInput = st.text_input(':green[Type your answer as though it automatically has a *"this app allows users to..."* at the beginning. ex input: *find the closest farmers market*]')

#create and write output on button press
if st.button('**Generate ideas!**'):
    template = 'I am making an app named "' + nameInput + '" the purpose of this app is to allows users to ' + purposeInput + '. You are a graphic designer. Please generate three ideas for what an icon for my app could look like based on its name and purpose. The icon should be in the "flat icon" style, making it clean and modern. Be sure to describe the colors and imagery for each idea. Also include a short rational for why you chose the colors and imagery. Enumerate your three ideas in a list. Youre response should begin with: "Here are three ideas for your app icon"'
    res = llm(template)
    st.write(res)
    st.success("**Not the ideas you were looking for?**")
    st.warning("You can always click the button again to get new ideas. If you feel like the ideas are missing something, try adding double parentheses around words or phrases you want to emphasize. *This is an ((example))*")