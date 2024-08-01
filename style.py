import streamlit as st

st.image('Naira.jpeg', caption='Naira Symbol', width=60)
st.audio('audio.mp3')
st.video('video.mp4')

st.markdown("""
<style>
div{
    background: White;
    color: blue;
}
</style>     
""", unsafe_allow_html=True)