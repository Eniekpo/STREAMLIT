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
