
# Heart Disease Prediction API with 100% Accuracy

Welcome to the Heart Disease Prediction API, a project using FastAPI to predict whether a person has heart disease based on various health parameters. The prediction is made using a pre-trained **Random Forest model** loaded from a pickle file. The model training accuracy were **100%** and model testing accuracy were **97%.** 


## Technologies

- **Python** : Used to data pre-processing and train the machine learning model. 

- **FastAPI** : This is a high-performance web framework Used to building API with python

    To install FastAPI

    ```bash
        pip install fastapi
    ```

- **Uvicorn** : Uvicorn is a Asynchronous Server Gateway Interface (ASGI). It is design to run python web-applications. by using `uvicorn` can handle FastAPI requests more efficiently. 

    To install Uvicorn:

    ```bash
        pip install uvicorn
    ```

- **Anaconda-Terminal** : Used to create environment for running the code lines. 

- **Pandas** : Library for data manipulation and analysis 

- **Scikit-learn** : Library for machine learning, used for model training and prediction

- **Matplotlib/Seaborn** : Libraries for data visualization.

## File Structure

- **__pycache__** : The `__pycache__` directory is automatically created by Python when you run a script. It stores compiled bytecode files (.pyc files) for each Python module that has been imported. 

- **FastApiModel.py** : API script. 

  To run the API using uvicorn 

  ```bash
    if __name__ == '__main__':
      uvicorn.run(app, host='127,0,0,1', port=8000)
  ```

  To Deployee the FastAPI in Localhost

  ```bash
    uvicorn FastApiModel:app --reload
  ```

- **HeartDiseases.py** : This is a data model file. In this file consists all the parameters of model.

  HeartDiseases.py

  ```bash
    from pydantic import BaseModel

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
  ```
- **RandomForest.pkl** : This is a trained model. save as a pickel file. 

- **heart.xlx** : dataset

- **requirnments.txt** : All the libraries and their's versions. 

  By using anaconda-terminal can create requirnments.txt file.

  ```bash
    pip freeze > requirnments.txt
  ```

## API endpoints

1. Index Page

- URL : '/'
- Method : Get
- Response: 

    ```bash
      "message" : "Welcome to FastAPI"
    ```

2. Predict Heart Disease

- URL : '/predict'
- Method : Post
- Response:

    ```bash
       "prediction": "The person does not have a  Heart Disease"
    ```


## Deployment to Render

- Created a Render account by using Git hub authentications. 
- Connected GitHub repository called "Heart Disease Prediction API with 100% Accuracy" 
- Finally deployee the GitHub repository to Render Cloud.

  ![render_deploying](https://github.com/user-attachments/assets/e4974661-e8ca-4165-ae35-c4e359eff7d7)

  **Visit to the API:**

  - [Goto Index Page](https://fastapi-application-ktuz.onrender.com/)

  - [Goto Predict page](https://fastapi-application-ktuz.onrender.com/docs)


  


## Acknowledgements

 - [FastAPI Documentation](https://fastapi.tiangolo.com/)
 - [Uvicorn Documentation](https://www.uvicorn.org/)
 - [Render Documentation](https://docs.render.com/)


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/)
 License

