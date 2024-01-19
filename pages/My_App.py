import os
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title('My App in Streamlit')

fl = st.file_uploader(":file_folder: Upload a File", type=(["csv", "txt", "xlsx", "xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_excel(filename)
else:
    os.chdir(r"C:\Users\YOLETECH\Dropbox\STREAMLIT")
    df = pd.read_csv('Sales_report.csv')

# Inspect the raw data
st.subheader('Raw data')
st.write(df)

# Draw a Pie Chart
st.header('Profit By Location')

fig = px.pie(df, values = 'Profit', names="Sale_Location", hole=0.5)
fig.update_traces(text=df['Profit'], textposition='outside')
st.plotly_chart(fig, use_container_width=True)

# A bar Chart
st.subheader("Profit By Location")
fig = px.bar(df, x = 'Sale_Location', y = 'Profit' ,template='seaborn')
st.plotly_chart(fig, use_container_width=True, height = 200)

# A Line Chart
st.subheader('Profit By Month')
fig = px.line(df, x='Month', y='Profit', labels={'Profit': 'Monthly Profit'}, height=500, width=1000, template='gridon')
st.plotly_chart(fig, use_container_width=True)

# Create a treemap based on Region, Category and Sub-Category
st.subheader('Hierachical view of Profit using TreeMap')
fig = px.treemap(df, path=['Month', 'Sale_Location', 'Product_Description'], values='Profit', hover_data=['Profit'],
                  color='Product_Description')
fig.update_layout(width=800, height=650)
st.plotly_chart(fig, use_container_width=True)


# Create a scatter plot
data1 = px.scatter(df, x = "Sale_Location", y = "Profit", size = "Commission")
data1['layout'].update(title="Relationship between Sales and Profits using Scatter Plot.",
                       titlefont = dict(size=20),xaxis = dict(title="Profit",titlefont=dict(size=19)),
                       yaxis = dict(title = "Profit", titlefont = dict(size=19)))
st.plotly_chart(data1,use_container_width=True)

with st.expander("View Data"):
    st.write(df.iloc[:200,1:20:2].style.background_gradient(cmap="Oranges"))

# Download orginal DataSet
csv = df.to_csv(index = False).encode('utf-8')
st.download_button('Download Data', data = csv, file_name = "Data.csv",mime = "text/csv")
