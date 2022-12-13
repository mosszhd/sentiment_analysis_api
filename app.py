from flask import Flask, request, jsonify
from src.main import Prediction
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is my first API call!'

@app.route('/predict', methods=["POST"])
def predict():
    prediction_obj = Prediction()
    input_json = request.get_json(force=True) 
    print('nput json',input_json)
    result = prediction_obj.get_prediction(input_json['text'])
    dictToReturn = {'Prediction':result}
    return jsonify(dictToReturn)

app.run()