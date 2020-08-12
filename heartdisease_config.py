# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 17:32:05 2020

@author: rkbra
"""

MODEL_NAME = "./models/heart.pickle"

# target feature
TARGET = "target"

# features
FEATURES = [
    "age",
    "resting_blood_pressure",
    "cholesterol",
    "max_heart_rate_achieved",
    "st_depression",
    "num_major_vessels",
    "sex_male",
    "chest_pain_type_atypical angina",
    "chest_pain_type_non-anginal pain",
    "chest_pain_type_typical angina",
    "fasting_blood_sugar_lower than 120mg/dl",
    "rest_ecg_left ventricular hypertrophy",
    "rest_ecg_normal",
    "exercise_induced_angina_yes",
    "st_slope_flat",
    "st_slope_upsloping",
    "thalassemia_normal",
    "thalassemia_reversable defect",
]

FORM_INPUT = [
    {"label": "Please state your sex:", "input": "age", "type": "text"},
    {
        "label": "The person's sex",
        "input": "sex",
        "type": "select",
        "option": ["male", "female"],
    },
    {
        "label": "What type of chest pain do you have?",
        "input": "chest_pain_type",
        "type": "select",
        "option": [
            "typical angina",
            "asymptomatic",
            "non-anginal pain",
            "atypical angina",
        ],
    },
    {
        "label": "What is your resting blood pressure?",
        "input": "resting_blood_pressure",
        "type": "text",
    },
    {
        "label": "What is your cholesterol measurement in mg/dl?",
        "input": "cholesterol",
        "type": "text",
    },
    {
        "label": "What is your fasting blood sugar?",
        "input": "fasting_blood_sugar",
        "type": "select",
        "option": ["greater than 120mg/dl", "lower than 120mg/dl"],
    },
    {
        "label": "Select resting electrocardiographic measurement",
        "input": "rest_ecg",
        "type": "select",
        "option": ["left ventricular hypertrophy", "normal", "ST-T wave abnormality"],
    },
    {
        "label": "What is the max heart rate achieved?",
        "input": "max_heart_rate_achieved",
        "type": "text",
    },
    {
        "label": "Do you have exercise induced angina?",
        "input": "exercise_induced_angina",
        "type": "select",
        "option": ["yes", "no"],
    },
    {
        "label": "ST depression induced by exercise relative to rest:",
        "input": "st_depression",
        "type": "text",
    },
    {
        "label": "Select the slope of the peak exercise ST segment:",
        "input": "st_slope",
        "type": "select",
        "option": ["downsloping", "flat", "upsloping"],
    },
    {
        "label": "The number of major vessels",
        "input": "num_major_vessels",
        "type": "text",
    },
    {
        "label": "Select the level of thalassemia:",
        "input": "thalassemia",
        "type": "select",
        "option": ["fixed defect", "normal", "reversable defect"],
    },
]

# variables to transform
LOG_VARIABLES = [
    "age",
    "resting_blood_pressure",
    "cholesterol",
    "max_heart_rate_achieved",
    "st_depression",
]

# numerical features
NUMERICAL_FEATURES = [
    "age",
    "resting_blood_pressure",
    "cholesterol",
    "max_heart_rate_achieved",
    "st_depression",
    "num_major_vessels",
]

# categorical features
CATEGORICAL_FEATURES = [
    "sex",
    "chest_pain_type",
    "fasting_blood_sugar",
    "rest_ecg",
    "exercise_induced_angina ",
    "st_slope ",
    "thalassemia",
]
