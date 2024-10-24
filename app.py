from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware

origins = ['*']

app = FastAPI(title='Fitness Tracker')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

model = load(pathlib.Path('model/fitness-traker-v1.joblib'))

class InputData(BaseModel):
    Accelerometer_x: float 
    Accelerometer_y: float 
    Accelerometer_z: float  
    Gyroscope_x: float      
    Gyroscope_y: float      
    Gyroscope_z: float      

class OutputData(BaseModel):
    score: float

@app.post('/score', response_model=OutputData)
def score(data: InputData):
    model_input = np.array([[data.Accelerometer_x, data.Accelerometer_y, 
                              data.Accelerometer_z, data.Gyroscope_x, 
                              data.Gyroscope_y, data.Gyroscope_z]])
    
    print("Input to model:", model_input)  
    result = model.predict_proba(model_input)[:, -1]  
    print("Model prediction result:", result)  

    return OutputData(score=float(result[0])) 