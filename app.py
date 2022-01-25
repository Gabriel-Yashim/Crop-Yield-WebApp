# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 15:24:33 2022

@author: YASHIM GABRIEL
"""

import numpy as np 
from flask import Flask, request, render_template
import pickle
from logging import FileHandler,WARNING

app = Flask(__name__)
model = pickle.load(open('GradientBoost.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

@app.route('/predict',methods=['POST'])
def predict():   
     N = int(request.form['nitrogen'])
     P = int(request.form['phosphorous'])
     K = int(request.form['pottasium'])
     Temperature = float(request.form['temperature'])
     Humidity = float(request.form['humidity'])
     ph = float(request.form['ph'])
     rainfall = float(request.form['rainfall'])
    
     final_features = np.array([[N,P,K,Temperature,Humidity,ph,rainfall]])
     prediction = model.predict(final_features)
    
     output = prediction[0]
    
     return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)