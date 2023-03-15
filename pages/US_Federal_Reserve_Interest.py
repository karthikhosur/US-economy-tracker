import streamlit as st
import data
import pandas as pd
import plotly.subplots as sp
import plotly.graph_objects as go
from datetime import date, datetime
import plotly.express as px

# Config
st.set_page_config(page_title='Macro - Cross Chain Monitoring',
                   page_icon=':bar_chart:', layout='wide')
global date_range
# Title
st.title('US Federal Reserve Interest')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

fed_rate_basic = data.get_data('fed_rate_basic')

# Load the data
data, df_all = fed_rate_basic
data.dropna(inplace=True)
df_all.dropna(inplace=True)
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y').dt.date
# App title
st.title("Financial Rates Dashboard")
# Multiselect for rate types
selected_types = st.multiselect(
    "Select Rate Types", options=data['Type'].unique(), default=['EFFR'])

# Filter data based on selected rate types
filtered_data = data[data['Type'].isin(selected_types)]
print(type(data['Date'].min()))
# Date range slider
start_date, end_date = st.slider("Select Date Range", min_value=data['Date'].min(
), max_value=data['Date'].max(), value=(data['Date'].min(), data['Date'].max()))
print(start_date, end_date)
# # Filter data based on selected date range
# print(filtered_data['Date'])
filtered_data = filtered_data[(filtered_data['Date'] >= start_date) & (
    filtered_data['Date'] <= end_date)]
print(filtered_data['Date'])

# Create a plotly figure
fig = go.Figure()
fig2 = go.Figure()

for rate_type in selected_types:
    rate_data = filtered_data[filtered_data['Type'] == rate_type]
    fig.add_trace(go.Scatter(
        x=rate_data['Date'], y=rate_data['Rate'], mode='lines', name=rate_type))

    # fig2.add_trace(go.Figure(data=[go.Candlestick(x=df_all['Date'],
    #                                               open=df_all['open'],
    #                                               high=df_all['high'],
    #                                               low=df_all['low'],
    #                                               close=df_all['close'])]))


fig.update_layout(
    title="Federal Rates by Date",
    xaxis_title="Date",
    yaxis_title="Rate (%)", dragmode=False
)

# Show the plot in Streamlit
st.plotly_chart(fig, use_container_width=True, theme="streamlit")
# st.plotly_chart(fig2, use_container_width=True, theme="streamlit")

# Show the filtered data in a table
# st.write(filtered_data)
