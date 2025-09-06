# app.py
from flask import Flask, request, render_template
import pickle
import pandas as pd

# Load trained model
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # A simple HTML form

@app.route("/predict", methods=["POST"])
def predict():
    try:
        size = float(request.form["size"])  # input from form
        test_data = pd.DataFrame({"size": [size]})  # keep column name
        price = model.predict(test_data)[0]
        return f"Predicted House Price: ₹ {round(price, 2)}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
