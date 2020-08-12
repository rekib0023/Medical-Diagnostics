# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 20:52:27 2020

@author: rkbra
"""

MODEL_NAME = "./models/liver.pickle"

# target feature
TARGET = 'Target'

# features
FEATURES = ['Age', 'Total_Bilirubin', 'Alkaline_Phosphotase',
            'Alamine_Aminotransferase', 'Total_Protiens', 'Albumin',
            'Albumin_and_Globulin_Ratio', 'Gender_Male']

FORM_INPUT = [
    {'label':'Age', 'input': 'Age', 'type': 'text'},
    {'label':'Total Bilirubin', 'input': 'Total_Bilirubin', 'type': 'text'},
    {'label':'Alkaline Phosphotase', 'input': 'Alkaline_Phosphotase', 'type': 'text'},
    {'label':'Alamine Aminotransferase', 'input': 'Alamine_Aminotransferase', 'type': 'text'},
    {'label':'Total Protiens', 'input': 'Total_Protiens', 'type': 'text'},
    {'label':'Albumin', 'input': 'Albumin', 'type': 'text'},
    {'label':'Albumin and Globulin Ratio', 'input': 'Albumin_and_Globulin_Ratio', 'type': 'text'},
    {'label':'Gender(Male/Female)', 'input': 'Gender', 'type': 'text'},
]