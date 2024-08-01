import streamlit as st

st.title('Uploading Files')
st.markdown("---")

Image = st.file_uploader('Please Upload an Image', type=['png', 'jpg'])
if Image is not None:
    st.image(Image)
    
Image = st.file_uploader('Please Upload an Image', type=['png', 'jpg'], accept_multiple_files=True)
for img in Image:
    st.image(img)

Video = st.file_uploader('Please Upload an Image', type='mp4')
if Video is not None:
    st.video(Video)