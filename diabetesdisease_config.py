# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 01:44:19 2020

@author: rkbra
"""

MODEL_NAME = "./models/diabetes.pickle"


# target feature
TARGET = 'Outcome'

# features
FEATURES = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
            'BMI', 'DiabetesPedigreeFunction', 'Age']

FORM_INPUT = [
    {'label': 'Number of times pregnant', 'input': 'Pregnancies', 'type': 'text'},
    {'label': 'Plasma glucose concentration', 'input': 'Glucose', 'type': 'text'},
    {'label': 'Diastolic blood pressure (mm Hg)', 'input': 'BloodPressure', 'type': 'text'},
    {'label': 'Triceps skin fold thickness (mm)', 'input': 'SkinThickness', 'type': 'text'},
    {'label': '2-Hour serum insulin (mu U/ml)', 'input': 'Insulin', 'type': 'text'},
    {'label': 'Body mass index (weight in kg/(height in m)^2)', 'input': 'BMI', 'type': 'text'},
    {'label': 'Diabetes pedigree function', 'input': 'DiabetesPedigreeFunction', 'type': 'text'},
    {'label': 'Age (years)', 'input': 'Age', 'type': 'text'}
]