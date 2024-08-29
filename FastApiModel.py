
# import Libraries

import uvicorn
from fastapi import FastAPI
from HeartDiseases import HeartDiseases
import numpy as np
import pickle
import pandas as pd

# create a app Object
app = FastAPI()

# load the model as pickel file
pickelFile = open("RandomForest_Model.pkl", "rb")
classifier = pickle.load(pickelFile)

# Index Page
@app.get('/')
def index():
    return {'message': 'Welcome to FastAPI'}

# return the single parameter
@app.get('/{name}')
def get_name(name: str):
    return{'message': f'Hello, {name}'} 

@app.post('/predict')
def predict_heartdiseases(data:HeartDiseases):
    data = data.dict()
    age = data['age']
    sex = data['sex']
    cp = data['cp']
    trestbps = data['trestbps']
    chol = data['chol']
    fbs = data['fbs']
    restecg = data['restecg']
    thalach = data['thalach']
    exang = data['exang']
    oldpeak = data['oldpeak']
    slope = data['slope']
    ca = data['ca']
    thal = data['thal']
    # print(classifier.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]))
    prediction = classifier.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    if(prediction[0] == 0):
        prediction = "The person does not have a Heart Disease"
    else:
        prediction = "The Person has a Heart Disease"
    return{
        'prediction' : prediction
    }

# Run the API using Uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127,0,0,1', port=8000)

# run the model - uvicorn FastApiModel:app --reload


