import os
import sys
from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None

    if request.method == "POST":
        try:
            # Get form data
            gender = request.form.get("gender")
            race_ethnicity = request.form.get("race_ethnicity")
            parental_education = request.form.get("parental_level_of_education")
            lunch = request.form.get("lunch")
            test_preparation_course = request.form.get("test_preparation_course")
            reading_score = request.form.get("reading_score")
            writing_score = request.form.get("writing_score")

            data = CustomData(
                gender=gender,
                race_ethnicity_group = race_ethnicity,
                parental_level_of_education=parental_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            pred_df = data.get_data_as_data_frame()
            predict_pipeline = PredictPipeline()
            prediction = predict_pipeline.predict(pred_df)[0]  # get scalar

            print(f"Prediction Result: {prediction}")

            return render_template("index.html",
                prediction=prediction,
                selected_gender=gender,
                selected_race_ethnicity=race_ethnicity,
                selected_parental_education=parental_education,
                selected_lunch=lunch,
                selected_test_preparation=test_preparation_course,
                selected_reading_score=reading_score,
                selected_writing_score=writing_score
            )
        except Exception as e:
            print("Error during prediction:", str(e))

    # Initial GET request
    return render_template("index.html", prediction = prediction)

if __name__ == "__main__":
    app.run(debug = True)
