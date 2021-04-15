import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st 
import time

data = pd.read_csv("data/csv")

def convert(x):
    year, week = x.split("-")
    year = (int(year) - 2020) * 54
    return year + int(week)

data['week'] = data.year_week.apply(lambda x: convert(x))

hun = data[data.country == 'Hungary']

fig = px.line(data_frame = hun, x = 'week', y = 'cumulative_count', color = 'indicator')




st.title("Hello World!")
country = st.selectbox("Select a country",["Hungary", "Belgium"])
st.write(f"The selected country is: {country}")
st.plotly_chart(fig)