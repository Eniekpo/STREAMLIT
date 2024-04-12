import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

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

# Show Data 
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# View and Download Data
with st.expander("View Data"):
    st.write(data.iloc[:200,1:20:2].style.background_gradient(cmap="Oranges"))

# Download orginal DataSet
csv = data.to_csv(index = False).encode('utf-8')
st.download_button('Download Data', data = csv, file_name = "Data.csv",mime = "text/csv")

st.subheader('SALES DASHBOARD')

# Draw a Pie Chart
st.header('Profit By Month')

fig = px.pie(data, values = 'profit', names='month', hole=0.5)
fig.update_traces(text=data['profit'], textposition='outside')
st.plotly_chart(fig, use_container_width=True)

# A bar Chart
st.subheader("Profit By Location")
fig = px.bar(data, x = 'sale_location', y = 'profit' ,template='seaborn')
st.plotly_chart(fig, use_container_width=True, height = 200)

# A Column Chart
st.subheader('Profit By Education')
fig = px.bar(data, x = 'education', y = 'profit' ,template='seaborn')
st.plotly_chart(fig, use_container_width=True, height = 200)

# Create a treemap based on Region, Category and Sub-Category
st.subheader('Hierachical view of Profit using TreeMap')
fig = px.treemap(data, path=['month', 'sale_location', 'education'], values='profit', hover_data=['profit'],
                  color='education')
fig.update_layout(width=800, height=650)
st.plotly_chart(fig, use_container_width=True)


# Create a scatter plot
data1 = px.scatter(data, x = "sale_location", y = "profit", size = "commission")
data1['layout'].update(title="Relationship between Sales and Profits using Scatter Plot.",
                       titlefont = dict(size=20),xaxis = dict(title="Profit",titlefont=dict(size=19)),
                       yaxis = dict(title = "Profit", titlefont = dict(size=19)))
st.plotly_chart(data1,use_container_width=True)

