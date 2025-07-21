import os 
import sys 
from flask import Flask, request, render_template
import numpy as np 
import pandas as pd 

from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    gender = ['male', 'female']
    race_ethnicity = ['group A', 'group B', 'group C', 'group D', 'group E']
    parental_education = ['bachelor', 'some_college', 'masters', 'associates', 'high_school', 'some_high_school']
    lunch = ['standard', 'free/reduced']
    test_preparation = ['completed', 'none']
    
    predicted_score = None

    return render_template(
        'index.html',
        gender = gender,
        race_ethnicity = race_ethnicity,
        parental_level_of_education = parental_education,
        lunch = lunch,
        test_preparation_course = test_preparation,
        predicted_score = predicted_score
    )

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        data = CustomData(
            gender = request.form.get('gender'),
            race_ethnicity_group = request.form.get('race_ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = int(request.form.get('reading_score')),
            writing_score = int(request.form.get('writing_score'))
        )

        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        # Render with predicted score
        gender = ['male', 'female']
        race_ethnicity = ['group A', 'group B', 'group C', 'group D', 'group E']
        parental_education = ['bachelor', 'some_college', 'masters', 'associates', 'high_school', 'some_high_school']
        lunch = ['standard', 'free/reduced']
        test_preparation = ['completed', 'none']

        return render_template(
            'index.html',
            gender = gender,
            race_ethnicity_group = race_ethnicity,
            parental_level_of_education = parental_education,
            lunch = lunch,
            test_preparation_course = test_preparation,
            predicted_score = result[0]  
        )

    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug = True)
