import pandas as pd
import plotly.express as px
import streamlit as st 

@st.cache
def load_data():
    data = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv")
    data['week'] = data.year_week.apply(lambda x: convert(x))
    return data

def convert(x):
    year, week = x.split("-")
    year = (int(year) - 2020) * 54
    return year + int(week)

data = load_data()

hun = data[data.country == 'Hungary']

st.title("Covid19 National Case-Death Data")

countries = data['country'].unique()
country_choice = st.sidebar.selectbox('Select the country:', countries)

fig = px.line(data_frame = hun, x = 'week', y = 'cumulative_count', color = 'indicator')
st.plotly_chart(fig)



