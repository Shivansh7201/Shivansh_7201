import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://avatars.githubusercontent.com/u/105603160?v=4)](https://gitHub.com/Shivansh7201/Shivansh_7201)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Shivansh Gupta, U.G')

st.info('ML Enthusiat, Content Creator with an interest in Data Science and AI..')

icon_size = 20

st_button('Youtube', 'https://youtube.com/@codekarr101', 'Data Professor YouTube channel', icon_size)
st_button('Medium', 'https://medium.com/@shivanshmay2019/', 'Read my Blogs', icon_size)
st_button('Twitter', 'https://twitter.com/shivansh7201', 'Follow me on Twitter', icon_size)
st_button('Linkedin', 'https://www.linkedin.com/in/shivansh-gupta-2a339b227/', 'Follow me on LinkedIn', icon_size)
st_button('Github', 'https://github.com/Shivansh7201/', 'CheckOut my new repository', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/shivansh7201', 'Buy me a Coffee', icon_size)
