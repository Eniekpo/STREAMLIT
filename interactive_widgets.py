import streamlit as st

state=st.checkbox('Female', value=False)
if state:
    st.markdown("""
        <h1>Hello Friends</h1>     
""", unsafe_allow_html=True)
else:
    print('Welcome Friends!')
    
# Other Properties of checkbox
# def change():
#     print('Changed')
# st.checkbox('Male', value=True, on_change=change)

def status():
    print(st.session_state.checker)
    
st.checkbox('Male', value=True, key=status)

radio_btn = st.radio('In which Country do you live?', options=('US', 'UK', 'Cananda'))
print(radio_btn)


def btn_click():
    print('Button Clicked')
btn=st.button('Click Me!', on_click=btn_click)

select=st.selectbox('What is your favorite food?', options=('Honda', 'Camry', 'Toyota', 'BMW'))
print(select)

multi_select=st.multiselect('What is your favorite kinds of music?', options=('R&B', 'Hip-Hop', 'Regae', 'Country Music'))

st.write(multi_select)

st.slider('Ratings', min_value=45, max_value=60, value=50)

val=st.text_input('Please Enter Your Name', max_chars=60)
print(val)

mytext=st.text_area('Course Description', max_chars=250)
print(mytext)

Date=st.date_input('Enter Your Registration Date')

Time=st.time_input('Set Timer')