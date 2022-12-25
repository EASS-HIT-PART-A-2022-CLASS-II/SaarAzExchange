import streamlit as st
from PIL import Image
import pandas as pd
import requests
import json

image = Image.open('logo.png')

st.image(image, width=500)

st.title('Saar Currency Converter App')
st.markdown("""Check how much your MONEY worth!""")
backend = "http://backend:8080/"

# Sidebar + Main panel
st.sidebar.header('Input Options')

currency_list = ['USD', 'ILS', 'GBP', 'EUR']

value = st.sidebar.number_input('Insert amount of currency')
f_value = float(value)
base_price_unit = st.sidebar.selectbox('Select base currency for conversion (FROM)', currency_list)
symbols_price_unit = st.sidebar.selectbox('Select target currency to convert to (TO)', currency_list)


@st.cache
def load_data():
    data = requests.get(f"{backend}currency/{base_price_unit}").json()
    base_currency = pd.Series(base_price_unit, name='FROM')
    to_currency = pd.Series(data['conversion_rates'], name='TO')
    specific_rate = pd.Series(to_currency[symbols_price_unit], name='RATE')
    f_specific_rate = float(specific_rate)
    final_value = (f_value * f_specific_rate)
    target_currency = pd.Series(symbols_price_unit, name='TO')
    conversion_date = pd.Series(data['time_last_update_utc'], name='DATE')
    sum_exchange = pd.Series(final_value, name='TOTAL')
    df = pd.concat([base_currency, target_currency, specific_rate, sum_exchange, conversion_date], axis=1)
    df.style.format()
    return df


df = load_data()

st.header('Currency conversion')

st.write(df)
