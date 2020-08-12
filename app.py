# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:32:10 2020

@author: rkbra
"""

from flask import Flask, request, render_template, url_for
from flask import send_from_directory
import os
import numpy as np
import pandas as pd
from math import pi
import joblib
from werkzeug.utils import secure_filename
from tensorflow import keras

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input

import heartdisease_config as heart_config
import heartdisease_preprocessing as heart_pp
import diabetesdisease_config as diabetes_config
import cancer_config
import liverdisease_config as liver_config
from project_config import my_proj

heart_model = joblib.load(filename=heart_config.MODEL_NAME)
diabetes_model = joblib.load(filename=diabetes_config.MODEL_NAME)
cancer_model = joblib.load(filename=cancer_config.MODEL_NAME)
liver_model = joblib.load(filename=liver_config.MODEL_NAME)
malaria_model = load_model("./models/malaria_model.h5")
pneumonia_model = load_model("./models/pneumonia_model.h5")

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'


def predict_malaria(img_path, model):
    img = image.load_img(img_path, target_size=(100, 100))
    x = image.img_to_array(img)

    # Scaling
    x = x / 255
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    result = model.predict(x)
    predicted_class = np.argmax(result, axis=1)

    if predicted_class == 0:
        preds = "The Person is Infected With Malaria"
    else:
        preds = "The Person is not Infected With Malaria"

    return preds


@app.route('/malaria', methods=['GET', 'POST'])
def malaria_disease():
    if request.method == 'GET':
        return render_template('/pages/malaria.html', title="Malaria Disease")
    else:
        file = request.files['image']
        full_name = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(full_name)

        label = predict_malaria(img_path=full_name, model=malaria_model)
        return render_template('/pages/malaria_predict.html', image_file_name=file.filename, label=label, title="Malaria Disease")


def predict_pneumonia(img_path, model):
    img = image.load_img(img_path, target_size=(150, 150))
    x = image.img_to_array(img)

    # Scaling
    x = x / 255
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    result = model.predict(x)
    predicted_class = np.argmax(result, axis=1)

    if predicted_class == 0:
        preds = "The Person is Infected With pneumonia"
    else:
        preds = "The Person is not Infected With pneumonia"
    return preds


@app.route('/pneumonia', methods=['GET', 'POST'])
def pneumonia_disease():
    if request.method == 'GET':
        return render_template('/pages/pneumonia.html', title="Pneumonia Disease")
    else:
        file = request.files['image']
        full_name = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(full_name)

        label = predict_pneumonia(img_path=full_name, model=pneumonia_model)
        return render_template('/pages/pneumonia_predict.html', image_file_name=file.filename, label=label, title="Pneumonia Disease")


@app.route('/breast_cancer', methods=['GET', 'POST'])
def breast_cancer():
    json_data = {}
    result = None
    if request.method == 'POST':
        json_data['radius_mean'] = float(request.form['radius_mean'])
        json_data['texture_mean'] = float(request.form['texture_mean'])
        json_data['smoothness_mean'] = float(request.form['smoothness_mean'])
        json_data['compactness_mean'] = float(request.form['compactness_mean'])
        json_data['concavity_mean'] = float(request.form['concavity_mean'])
        json_data['concave_points_mean'] = float(request.form['concave_points_mean'])
        json_data['symmetry_mean'] = float(request.form['symmetry_mean'])
        json_data['fractal_dimension_mean'] = float(request.form['fractal_dimension_mean'])
        json_data['radius_se'] = float(request.form['radius_se'])
        json_data['texture_se'] = float(request.form['texture_se'])
        json_data['smoothness_se'] = float(request.form['smoothness_se'])
        json_data['compactness_se'] = float(request.form['compactness_se'])
        json_data['concavity_se'] = float(request.form['concavity_se'])
        json_data['concave_points_se'] = float(request.form['concave_points_se'])
        json_data['symmetry_se'] = float(request.form['symmetry_se'])
        json_data['fractal_dimension_se'] = float(request.form['fractal_dimension_se'])
        json_data['radius_worst'] = float(request.form['radius_worst'])
        json_data['texture_worst'] = float(request.form['texture_worst'])
        json_data['smoothness_worst'] = float(request.form['smoothness_worst'])
        json_data['compactness_worst'] = float(request.form['compactness_worst'])
        json_data['concavity_worst'] = float(request.form['concavity_worst'])
        json_data['concave_points_worst'] = float(request.form['concave_points_worst'])
        json_data['symmetry_worst'] = float(request.form['symmetry_worst'])
        json_data['fractal_dimension_worst'] = float(request.form['fractal_dimension_worst'])

        data = pd.DataFrame(json_data, index=[0])
        data.columns = cancer_config.FEATURES
        pred_proba = cancer_model.predict_proba(np.array(data.iloc[0]).reshape(1, -1))
        if pred_proba[0][1] > 0.3:
            result = "You have been diagnosed with Breast Cancer"
        else:
            result = "You are not being diagnosed with Breast Cancer"

    return render_template('/pages/cancer.html', props=cancer_config.FORM_INPUT, result=result,
                           title='Breast Cancer Detection')


@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    json_data = {}
    result = None
    if request.method == 'POST':
        json_data['Pregnancies'] = float(request.form['Pregnancies'])
        json_data['Glucose'] = float(request.form['Glucose'])
        json_data['BloodPressure'] = float(request.form['BloodPressure'])
        json_data['SkinThickness'] = float(request.form['SkinThickness'])
        json_data['Insulin'] = float(request.form['Insulin'])
        json_data['BMI'] = float(request.form['BMI'])
        json_data['DiabetesPedigreeFunction'] = float(request.form['DiabetesPedigreeFunction'])
        json_data['Age'] = float(request.form['Age'])

        data = pd.DataFrame(json_data, index=[0])
        pred_proba = diabetes_model.predict_proba(np.array(data.iloc[0]).reshape(1, -1))
        if pred_proba[0][1] > 0.3:
            result = "You have been diagnosed with Diabetes"
        else:
            result = "You are not being diagnosed with Diabetes"

    return render_template('/pages/diabetes.html', props=diabetes_config.FORM_INPUT, result=result,
                           title='Diabetes Detection')


@app.route('/heart', methods=['GET', 'POST'])
def heart_disease():
    json_data = {}
    result = None
    if request.method == 'POST':
        json_data['age'] = float(request.form['age'])
        json_data['sex'] = str(request.form['sex'])
        json_data['chest_pain_type'] = str(request.form['chest_pain_type'])
        json_data['resting_blood_pressure'] = float(request.form['resting_blood_pressure'])
        json_data['cholesterol'] = float(request.form['cholesterol'])
        json_data['fasting_blood_sugar'] = str(request.form['fasting_blood_sugar'])
        json_data['rest_ecg'] = str(request.form['rest_ecg'])
        json_data['max_heart_rate_achieved'] = float(request.form['max_heart_rate_achieved'])
        json_data['exercise_induced_angina'] = str(request.form['exercise_induced_angina'])
        json_data['st_depression'] = float(request.form['st_depression'])
        json_data['st_slope'] = str(request.form['st_slope'])
        json_data['num_major_vessels'] = float(request.form['num_major_vessels'])
        json_data['thalassemia'] = str(request.form['thalassemia'])

        data = pd.DataFrame(json_data, index=[0])
        data = heart_pp.log_transformer(data, variables=heart_config.LOG_VARIABLES)
        data = heart_pp.get_dummies(data)

        pred_proba = heart_model.predict_proba(np.array(data.iloc[0]).reshape(1, -1))
        if pred_proba[0][1] > 0.3:
            result = "You have been diagnosed with Heart Disease"
        else:
            result = "You are not being diagnosed with Heart Disease"

    return render_template('/pages/heart.html', props=heart_config.FORM_INPUT, result=result, title='Heart Detection')


@app.route('/liver', methods=['GET', 'POST'])
def liver_disease():
    json_data = {}
    result = None
    if request.method == 'POST':
        json_data['Age'] = float(request.form['Age'])
        json_data['Total_Bilirubin'] = float(request.form['Total_Bilirubin'])
        json_data['Alkaline_Phosphotase'] = float(request.form['Alkaline_Phosphotase'])
        json_data['Alamine_Aminotransferase'] = float(request.form['Alamine_Aminotransferase'])
        json_data['Total_Protiens'] = float(request.form['Total_Protiens'])
        json_data['Albumin'] = float(request.form['Albumin'])
        json_data['Albumin_and_Globulin_Ratio'] = float(request.form['Albumin_and_Globulin_Ratio'])
        # json_data['Gender'] = str(request.form['Gender'])
        if request.form['Gender'] == 'Male':
            json_data['Gender_Male'] = 1
        else:
            json_data['Gender_Male'] = 0

        data = pd.DataFrame(json_data, index=[0])

        for var in liver_config.FEATURES:
            data[var] = np.log1p(data[var])

        pred_proba = liver_model.predict_proba(np.array(data.iloc[0]).reshape(1, -1))
        if pred_proba[0][1] > 0.3:
            result = "You have been diagnosed with Liver Disease"
        else:
            result = "You are not being diagnosed with Liver Disease"

    return render_template('/pages/liver.html', props=liver_config.FORM_INPUT, result=result,
                           title='Liver Disease Detection')


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', props=my_proj)


@app.route('/predict_heart_disease_via_postman', methods=['POST'])
def predict_heart_disease_via_postman():
    if request.method == 'POST':
        json_data = request.get_json()
        data = pd.DataFrame(json_data, index=[0])
        data = heart_pp.log_transformer(data, variables=heart_config.LOG_VARIABLES)
        data = heart_pp.get_dummies(data)

        pred = heart_model.predict(np.array(data.iloc[0]).reshape(1, -1))
        pred_proba = heart_model.predict_proba(np.array(data.iloc[0]).reshape(1, -1))
        result = f'{pred} *** {pred_proba}'
    else:
        result = "Something went wrong!"
    return result


@app.route('/predict_diabetes_via_postman', methods=['POST'])
def predict_diabetes_via_postman():
    if request.method == 'POST':
        json_data = request.get_json()
        data = pd.DataFrame(json_data, index=[0])

        pred = diabetes_model.predict(np.array(data.iloc[0]).reshape(1, -1))
        pred_proba = diabetes_model.predict_proba(np.array(data.iloc[0]).reshape(1, -1))
        result = f'{pred} *** {pred_proba}'
    else:
        result = "Something went wrong!"
    return result


@app.route('/predict_cancer_via_postman', methods=['POST'])
def predict_cancer_via_postman():
    if request.method == 'POST':
        json_data = request.get_json()
        data = pd.DataFrame(json_data, index=[0])

        pred = cancer_model.predict(np.array(data.iloc[0]).reshape(1, -1))
        pred_proba = cancer_model.predict_proba(np.array(data.iloc[0]).reshape(1, -1))
        result = f'{pred} *** {pred_proba}'
    else:
        result = "Something went wrong!"
    return result


@app.route('/predict_liver_disease_via_postman', methods=['POST'])
def predict_liver_disease_via_postman():
    if request.method == 'POST':
        json_data = request.get_json()
        data = pd.DataFrame(json_data, index=[0])

        for var in liver_config.FEATURES:
            data[var] = np.log1p(data[var])

        pred = liver_model.predict(np.array(data.iloc[0]).reshape(1, -1))
        pred_proba = liver_model.predict_proba(np.array(data.iloc[0]).reshape(1, -1))
        result = f'{pred} *** {pred_proba}'
    else:
        result = "Something went wrong!"
    return result


if __name__ == '__main__':
    app.run(debug=True)
