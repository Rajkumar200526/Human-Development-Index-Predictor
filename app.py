from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model/hdi_model.pkl", "rb"))
df = pd.read_csv("dataset/clean_hdi.csv")

# ==========================
# Home Page
# ==========================
@app.route("/")
def home():
    return render_template("index.html")

# ==========================
# Prediction
# ==========================
@app.route("/predict", methods=["GET", "POST"])
def predict():

    countries = sorted(df["Country"].dropna().unique())

    if request.method == "POST":

        life = float(request.form["life"])
        expected = float(request.form["expected"])
        mean = float(request.form["mean"])
        gni = float(request.form["gni"])

        prediction = model.predict([[life, expected, mean, gni]])[0]

        if prediction >= 0.800:
            category = "Very High Human Development"
        elif prediction >= 0.700:
            category = "High Human Development"
        elif prediction >= 0.550:
            category = "Medium Human Development"
        else:
            category = "Low Human Development"

        return render_template(
            "result.html",
            prediction=round(prediction, 3),
            category=category
        )

    return render_template(
        "predict.html",
        countries=countries
    )
@app.route("/country/<country>")
def country(country):

    row = df[df["Country"] == country]

    if row.empty:
        return jsonify({})

    row = row.iloc[0]

    return jsonify({
        "life": row["LifeExpectancy"],
        "expected": row["ExpectedSchooling"],
        "mean": row["MeanSchooling"],
        "gni": row["GNI"]
    })
# ==========================
if __name__=="__main__":
    app.run(debug=True)