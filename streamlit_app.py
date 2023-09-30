# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 00:09:17 2023

@author: Gabriel Yashim
"""

import numpy as np 
import pickle
import streamlit as st


model = pickle.load(open('C:/Users/SHOPINVERSE/Documents/GitHub/Crop-Yield-WebApp/GradientBoost.pkl', 'rb'))


st.title('Crop Yield Prediction System')
html_temp = """
    <h3 style="color:white;text-align:center;">By Gabriel Yashim</h3>
    <div style="background-color:rgb(6, 138, 2);padding:10px;margin-bottom:3rem">
        <p style="text-align:justify;">
            Welcome to this simple Crop Yield Prediction System. The system can recommend the kind of crop you should plant based on some properties of the soil and weather conditions. <br> 
                This system can predict the following 23 different crops based on the input data supplied by the user to the system. <br>
                <ul style="display:grid; grid-gap:1rem; grid-template-columns: repeat(4, 1fr);">
                    <li>Rice</li>
                    <li>Cotton</li>
                    <li>Mungbean</li>
                    <li>Pigeonpeas</li>
                    <li>Orange</li>
                    <li>Maize</li>
                    <li>Mango</li>
                    <li>Cashew</li>
                    <li>Mothbeans</li>
                    <li>Watermelon</li>
                    <li>Jute/Ewedu</li>
                    <li>Kidneybeans</li>
                    <li>Black Beans</li>
                    <li>Grapes</li>
                    <li>Palm Tree</li>
                    <li>Papaya</li>
                    <li>Coconut</li>
                    <li>Banana</li>
                    <li>Beni/Sesame Seed</li>
                    <li>Muskmelon</li>
                    <li>Chickpea</li>
                    <li>Potato</li>
                    <li>Coffee</li>
                </ul>
        </p>  
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)



# Input field for column1
N = st.text_input("Nitrogen Level (an integer)")
P = st.text_input("Phosphorus Level (an integer)")
K = st.text_input("Potassium Level (an integer)")
Temperature = st.text_input("Temperature in Celcius (a float)")
Humidity = st.text_input("Humidity in grams per cubic meter (g/m³) (a float)")
ph = st.text_input("Soil pH Level(a float)")
rainfall = st.text_input("Rainfall in millimeters (mm) (a float)")
    


pred = ''

result = ''


if st.button('Submit'):
    pred = model.predict([[N,P,K,Temperature,Humidity,ph,rainfall]])
        
    st.write(f"The crop that is suitable for the soil is:  {pred[0]}")
    




