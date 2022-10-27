import streamlit as st
from functions import load_css,blog, st_button
from topics_list import topics_list
import video
import image
import description
import article

load_css()

st.header("Tech Talk")
st.subheader("A WEBSITE FOR LEARNING TECH TOPICS.")
st.image("https://media3.giphy.com/avatars/HeyAutoHQ/DgfrJNR8oUyv.gif")

selected_topic = st.selectbox('Select a Topic', topics_list)

index=topics_list.index(selected_topic)

img=image.image[index]
desc=description.description[index]
art=article.articles[index]
vid=video.videos[index]

st.subheader(selected_topic)

blog(selected_topic,img,desc)

st.subheader("LEARN FROM TECH ARTICLES")

st_button(art[0],"TECH ARTICLE 1")
st_button(art[1],"TECH ARTICLE 2")
st_button(art[2],"TECH ARTICLE 3")

st.subheader("LEARN FROM VIDEOS")

st.video(vid[0])
st.video(vid[1])
