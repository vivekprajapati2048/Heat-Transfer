# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:30:49 2021

@author: Vivek
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    PHP_Type_Tabular = 0
    
    if request.method == 'POST':
        
        inner_d = float(request.form['id'])
        od = float(request.form['od'])
        le = float(request.form['le'])
        lc = float(request.form['lc'])
        turn = float(request.form['turn'])
        fluid = float(request.form['fluid'])
        fr = float(request.form['fr'])
        orientation = float(request.form['orientation'])
        heatw = float(request.form['heatw'])
        
        PHP_Type_Flat_Plate = request.form['PHP_Type_Flat_Plate']
        if(PHP_Type_Flat_Plate == 'Tabular'):
            PHP_Type_Tabular = 1
        else:
            PHP_Type_Tabular = 0
            
        
        
        
        prediction=model.predict([[inner_d,od,le,lc,turn,fluid,fr,orientation,heatw,PHP_Type_Tabular]])
        output=round(prediction[0],10)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry no rth value")
        else:
            return render_template('index.html',prediction_text="rth: {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

