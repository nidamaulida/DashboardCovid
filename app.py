import streamlit as st
from data import *

def judul():
    st.title("😷 Dashboard Covid-19 Indonesia") 
    st.markdown("Selamat datang di dashboard interaktif untuk menganalisis data *Covid-19* di Indonesia.")

st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

if menu == "Home":
    judul()
    year = select_year()
    location = select_location()  
    df = load_data()
    df_filtered = filter_data(df, year, location)
    kolom(df_filtered)
    pie_chart1(df_filtered)
    bar_chart1(df_filtered)  
    bar_chart2(df_filtered)  
    map_chart(df_filtered, year) 

elif menu == "Halaman Data":
    judul()
    year = select_year()
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered)