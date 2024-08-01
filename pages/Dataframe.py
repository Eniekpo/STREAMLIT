import streamlit as st
import pandas as pd

table = pd.DataFrame({'Column': [1, 2, 3, 4, 5, 6, 7], "Column 2": [11, 12, 13, 14, 15, 16, 17]})

st.table(table)
st.dataframe(table)