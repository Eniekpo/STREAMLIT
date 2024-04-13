import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

# Create a Streamlit sidebar where the user can input parameters
st.sidebar.title('Plot Settings')
x_min = st.sidebar.number_input('Minimum X', value=0)
x_max = st.sidebar.number_input('Maximum X', value=10)
num_points = st.sidebar.number_input('Number of Points', value=50)

# Generate some sample data
x = np.linspace(x_min, x_max, num_points)
y = np.sin(x)

# Plot the data using Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Sinusoidal Curve')

# Display the plot using Streamlit
st.pyplot(fig)

st.sidebar.title('Bar Chart Settings')
num_bars = st.sidebar.slider('Number of Bars', min_value=1, max_value=10, value=5)

# Generate some sample data
x = np.arange(num_bars)
y = np.random.randint(1, 100, size=num_bars)

# Plot the data using Matplotlib
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Bar Chart')

# Display the plot using Streamlit
st.pyplot(fig)