import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Sales Dashboard", 
    page_icon=":file_folder:",
    )

st.title(" :bar_chart: YOLETECH HUB DATA ANALYTICS")
st.markdown('<style>div.block-container{padding-top: 1rem;}</style>', unsafe_allow_html=True)

# Loading The Data 
DATA_URL = ('Sales_report.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('DATA VISUALIZATIONS')
