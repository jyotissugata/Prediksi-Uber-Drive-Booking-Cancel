import streamlit as st
import eda, predict

st.set_page_config(page_title="Predict Booking Data", layout="centered")

with st.sidebar:
    st.write("# Page Navigation")
    option = st.selectbox('Page', ['EDA', 'Model Demo'])

    st.write('# About')
    st.write('Page ini adalah informasi data dan demo dari model prediksi Booking Cancel')

if option == 'EDA':
    eda.run()
else:
    predict.run()
