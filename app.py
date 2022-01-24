# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 15:24:33 2022

@author: YASHIM GABRIEL
"""

#import numpy as np 
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
    int_features = [int(x) for x in request.form.values()]
    final_features = [int_features]
    prediction = model.predict(final_features)
    
    output = prediction
    
    return render_template('index.html', prediction_text='The crop that will give the best yield is {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)