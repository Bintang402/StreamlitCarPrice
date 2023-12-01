
import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt


app_mode = st.sidebar.selectbox('Select Page',['Home','Dataset','Prediction']) 
if app_mode=='Home':    
    st.title("Welcome to Car Price Prediction! 👋")      
    st.image('Mustang.png')  

if app_mode=='Dataset':

    model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))
    st.markdown("Dataset")
    #open file csv
    df1 = pd.read_csv('CarPrice.csv')
    st.dataframe(df1)

    chart_highwaympg = pd.DataFrame(df1,columns=['highwaympg'])
    
    chart_curbweights = pd.DataFrame(df1,columns=['curbweight'])
    
    chart_horsepower = pd.DataFrame(df1,columns=['horsepower'])
    
    st.markdown("Chart")
    chart = st.selectbox('Pilih Grafik Yang Ingin Ditampilkan ', ['highwaympg','curbweight', 'horsepower'])
    if chart == 'highwaympg':
        st.write("Grafik Highway-mpg")
        st.line_chart(chart_highwaympg)
    
    if chart == 'curbweight':
        st.write("Grafik curbweights")
        st.line_chart(chart_curbweights)

    if chart == 'horsepower':
        st.write("Grafik horsepower")
        st.line_chart(chart_horsepower)
        
if app_mode=='Prediction': 

    model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))
    df1 = pd.read_csv('CarPrice.csv')


    #input nilai dari variable independent
    highwaympg = st.number_input ('Highway-mpg',0, 10000000)
    curbweight = st.number_input('Curbweights',0, 10000000)
    horsepower = st.number_input('Horsepower',0, 10000000)

    if st.button('Prediksi'):
        #prediksi variable yang telah diinputkan 
        car_prediction = model.predict([[highwaympg,curbweight,horsepower]])

        #convert ke string
        harga_mobil_str = np.array(car_prediction)
        harga_mobil_float = float(harga_mobil_str[0])
        #tampilkan hasil prediksi
        harga_mobil_formatted = "{:,.2f}".format(harga_mobil_float)
        st.markdown(f'Harga Mobil: ${harga_mobil_formatted}')