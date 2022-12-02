import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle
import streamlit as st
import streamlit.components.v1 as stc

app=Flask(__name__)
model=pickle.load(open("rf.pkl", "rb"))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    feature= [np.array(float_features)]
    prediction= model.predict(feature)
    return render_template("index.html", prediction_text="{}".format(prediction))

if __name__=="__main__":
    app.run(debug=True)