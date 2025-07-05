import json 
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

# Home route for HTML form
@app.route('/')
def home():
    return render_template('home.html')

# HTML form submission
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        data = [float(x) for x in request.form.values()]
        final_input = scalar.transform(np.array(data).reshape(1, -1))
        output = regmodel.predict(final_input)[0]
        return render_template("home.html", prediction_text=f"The predicted price of the house is $ {output:.2f}")
    except Exception as e:
        return render_template("home.html", prediction_text=f"Error: {str(e)}")

# API route for JSON input (e.g., Postman)
@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        # Get JSON and extract the 'data' dictionary
        content = request.get_json(force=True)
        data = content['data']

        input_features = [
            data['MedInc'],
            data['HouseAge'],
            data['AveRooms'],
            data['AveBedrms'],
            data['Population'],
            data['AveOccup'],
            data['Latitude'],
            data['Longitude']
        ]

        final_input = scalar.transform(np.array(input_features).reshape(1, -1))
        output = regmodel.predict(final_input)[0]
        return jsonify({"prediction": round(output, 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
