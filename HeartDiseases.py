
from pydantic import BaseModel

# class with describes all the parameters of model

class HeartDiseases(BaseModel):
    age : int
    sex : int
    cp : int
    trestbps : int
    chol : int
    fbs : int
    restecg : int
    thalach : int
    exang : int
    oldpeak : float
    slope : int
    ca : int
    thal : int