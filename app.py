from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def result():
    item_weight = float(request.form['item_weight'])
    item_fat_content = float(request.form['item_fat_content'])
    item_visibility = float(request.form['item_visibility'])
    item_type = float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    outlet_establishment_year = float(request.form['outlet_establishment_year'])
    outlet_size = float(request.form['outlet_size'])
    outlet_location_type = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])

    X = np.array([[item_weight, item_fat_content, item_visibility, item_type, item_mrp,
                   outlet_establishment_year, outlet_size, outlet_location_type, outlet_type]])

    model_path = 'random_forest_grid.sav'
    model = joblib.load(model_path)
    Y_pred = model.predict(X)

    # Pass the prediction value to predictions.html
    return render_template('predictions.html', prediction=float(Y_pred))

if __name__ == "__main__":
    app.run(debug=True, port=9457)