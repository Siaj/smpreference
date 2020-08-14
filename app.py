import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

import pickle

# load model
model = pickle.load(open('smprefmodel.pkl','rb'))

# app
app = Flask(__name__)
CORS(app)

# routes
@app.route('/preference', methods=['POST'])
def predict():
    # get data in json from request source
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'data': json_data, 'preference': str(result[0])}

    # return data
    return jsonify(results=output)

@app.route('/predict', methods=['GET'])

def get_predict():
    # get data
    data = {'Feedback': 4, 'Cues': 5, 'Language': 3, 'PFocus': 4} 
	# Should print Twitter
    json_data = data.copy();

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'data': json_data, 'preference': str(result[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
