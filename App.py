import streamlit as st

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Home Page", 
    page_icon=":file_folder:",
)
st.title(':bar_chart: YOLETECH HUB DATA ANALYSIS')

col1, col2 = st.columns(2)

with col1:
    # Create A Table
    st.subheader('Create Table')
    df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

    df

with col2:
    # Write a DataFrame
    st.subheader('Write a DataFrame')
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))