import streamlit as st 

st.markdown('<h1>Registration Form</h1>', unsafe_allow_html=True)
st.subheader('Method 1')

# METHOD 1

form = st.form('Form 1')
form.text_input('First Name')
form.text_input('Last Name')
form.text_input('Gender')
form.form_submit_button('Submit')

st.subheader('Method 2')
# METHOD 2
with st.form('Form 2'):
    st.text_input('First Name')
    st.text_input('Last Name')
    st.text_input('Gender')
    st.form_submit_button('Submit')
    
st.markdown('<h1>Streamlit Columns</h1>', unsafe_allow_html=True)
    
    