from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import sklearn
import numpy as np

app= Flask(__name__)
model= pickle.load(open("prediction_service/concrete_model.pkl","rb"))
@app.route("/", methods=["POST","GET"])
def Home():
    return render_template("index.html")
@app.route("/predict", methods=["POST","GET"])
def predict():
    if request.method=="POST":
        C= float(request.form["Cement (kg in a m^3 mixture)"])
        BFS= float(request.form["Blast Furnace Slag (kg in a m^3 mixture)"])
        FA= float(request.form["Fly Ash (kg in a m^3 mixture)"])
        W= float(request.form["Water (kg in a m^3 mixture)"])
        SUP= float(request.form["Superplasticizer (kg in a m^3 mixture)"])
        CAR= float(request.form["Coarse Aggregate (kg in a m^3 mixture)"])
        FAR= float(request.form["Fine Aggregate (kg in a m^3 mixture)"])
        A= float(request.form["Age (Days)"])
        prediction= float(model.predict([[C,BFS,FA,W,SUP,CAR,FAR,A]]))
        prediction= round(prediction,3)
        return render_template("index.html",prediction_text="Concrete Compressive Strength (in MPa)= {}".format(prediction))
    else:
        return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)