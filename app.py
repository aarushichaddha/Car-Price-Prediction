from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open("prediction_model.pkl", "rb"))

# Load feature columns
columns = pickle.load(open("columns.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])
    present_price = float(request.form["present_price"])
    kms = int(request.form["kms"])
    owner = int(request.form["owner"])

    fuel = request.form["fuel"]
    seller = request.form["seller"]
    transmission = request.form["transmission"]

    # Initialize all features to 0
    data = dict.fromkeys(columns, 0)

    # Fill numerical features
    if "Present_Price" in data:
        data["Present_Price"] = present_price

    if "Kms_Driven" in data:
        data["Kms_Driven"] = kms

    if "Driven_kms" in data:
        data["Driven_kms"] = kms

    if "Owner" in data:
        data["Owner"] = owner

    if "Car_Age" in data:
        data["Car_Age"] = age

    # Fuel Type
    fuel1 = "Fuel_Type_" + fuel
    if fuel1 in data:
        data[fuel1] = 1

    # Seller Type
    seller1 = "Seller_Type_" + seller
    if seller1 in data:
        data[seller1] = 1

    seller2 = "Selling_type_" + seller
    if seller2 in data:
        data[seller2] = 1

    # Transmission
    trans = "Transmission_" + transmission
    if trans in data:
        data[trans] = 1

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Arrange columns exactly as during training
    df = df[columns]

    # Prediction
    prediction = model.predict(df)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)