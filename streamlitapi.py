import streamlit as st
import requests

st.write("My First API")

r = requests.get('http://127.0.0.1:5000/api/quote')
myresponse = r.json()

st.write(myresponse['quote'])