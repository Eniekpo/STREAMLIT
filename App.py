import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Sales Dashboard", 
    page_icon=":file_folder:",
    )

st.title(" :bar_chart: YOLETECH HUB DATA ANALYTICS")
st.markdown('<style>div.block-container{padding-top: 1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a File", type=(["csv", "txt", "xlsx", "xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_excel(filename)
else:
    os.chdir(r"C:\Users\YOLETECH\Dropbox\STREAMLIT")
    df = pd.read_excel('Sales_report.csv')

col1, col2 = st.columns((2))
df["Month"] = pd.to_datetime(df["Month"])

# Getting the MIN and MAX Date
startDate = pd.to_datetime(df["Month"]).min()
endDate = pd.to_datetime(df["Month"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input('Start Date', startDate))

with col2:
    date2 = pd.to_datetime(st.date_input('End Date', endDate))

df = df[(df["Month"] >= date1) & (df["Month"] <= date2)].copy()