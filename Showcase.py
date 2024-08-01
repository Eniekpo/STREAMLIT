import streamlit as st 
import pandas as pd 

st.write("""
         # My First App
         Hello *World*
         """)

df = pd.read_csv('titanic.csv')
st.line_chart(df['Fare'])