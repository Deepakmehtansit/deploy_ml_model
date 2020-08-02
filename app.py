import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('adclick_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    dict_var = ["Daily Time Spent on Site", "Age", "Area Income", "Daily Internet Usage", "City", "Male", "Country"]
    features = [x for x in request.form.values()]
    int_features = []
    for i,j in enumerate(features):
        if (i == 0):
            int_features.append(float(j))
        elif (i==1):
            int_features.append(int(j))
        elif (i==2):
            int_features.append(float(j))
        elif (i==3):
            int_features.append(float(j))
        elif (i==4):
            int_features.append(int(j))
        elif (i==5):
            int_features.append(int(j))
        elif (i==6):
            int_features.append(int(j))
        else:
            pass
    print(int_features)
    out_var = dict(zip(dict_var,int_features))
    print(out_var)
    lsit_var = []
    lsit_var.append(out_var)
    print(lsit_var)
    final_features = pd.DataFrame(lsit_var)
    print(final_features)
    prediction = model.predict(final_features)
    print(prediction)
    output = prediction.item()

    return render_template('index.html', prediction_text='adclick prediction be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)