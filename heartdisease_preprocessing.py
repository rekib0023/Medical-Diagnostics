# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:21:21 2020

@author: rkbra
"""

import numpy as np


def log_transformer(X, variables=None):
    for var in variables:
        X[var] = np.log1p(X[var])

    return X


def get_dummies(X):
    if X['sex'][0] == 'male':
        X['sex_male'] = 1
    else:
        X['sex_male'] = 0
    X.drop('sex', 1, inplace=True)

    if X['chest_pain_type'][0] == 'atypical angina':
        X['chest_pain_type_atypical angina'] = 1
        X['chest_pain_type_non-anginal pain'] = 0
        X['chest_pain_type_typical angina'] = 0
    elif X['chest_pain_type'][0] == 'non-anginal angina':
        X['chest_pain_type_atypical angina'] = 0
        X['chest_pain_type_non-anginal pain'] = 1
        X['chest_pain_type_typical angina'] = 0
    elif X['chest_pain_type'][0] == 'typical angina':
        X['chest_pain_type_atypical angina'] = 0
        X['chest_pain_type_non-anginal pain'] = 0
        X['chest_pain_type_typical angina'] = 1
    else:
        X['chest_pain_type_atypical angina'] = 0
        X['chest_pain_type_non-anginal pain'] = 0
        X['chest_pain_type_typical angina'] = 0
    X.drop('chest_pain_type', 1, inplace=True)

    if X['fasting_blood_sugar'][0] == 'lower than 120mg/dl':
        X['fasting_blood_sugar_lower than 120mg/dl'] = 1
    else:
        X['fasting_blood_sugar_lower than 120mg/dl'] = 0
    X.drop('fasting_blood_sugar', 1, inplace=True)

    if X['rest_ecg'][0] == 'left ventricular hypertrophy':
        X['rest_ecg_left ventricular hypertrophy'] = 1
        X['rest_ecg_normal'] = 0
    elif X['rest_ecg'][0] == 'normal':
        X['rest_ecg_left ventricular hypertrophy'] = 0
        X['rest_ecg_normal'] = 1
    else:
        X['rest_ecg_left ventricular hypertrophy'] = 0
        X['rest_ecg_normal'] = 0
    X.drop('rest_ecg', 1, inplace=True)

    if X['exercise_induced_angina'][0] == 'yes':
        X['exercise_induced_angina_yes'] = 1
    else:
        X['exercise_induced_angina_yes'] = 0
    X.drop('exercise_induced_angina', 1, inplace=True)

    if X['st_slope'][0] == 'flat':
        X['st_slope_flat'] = 1
        X['st_slope_upsloping'] = 0
    elif X['st_slope'][0] == 'upsloping':
        X['st_slope_flat'] = 0
        X['st_slope_upsloping'] = 1
    else:
        X['st_slope_flat'] = 0
        X['st_slope_upsloping'] = 0
    X.drop('st_slope', 1, inplace=True)

    if X['thalassemia'][0] == 'normal':
        X['thalassemia_normal'] = 1
        X['thalassemia_reversable defect'] = 0
    elif X['thalassemia'][0] == 'reversable defect':
        X['thalassemia_normal'] = 0
        X['thalassemia_reversable defect'] = 1
    else:
        X['thalassemia_normal'] = 0
        X['thalassemia_reversable defect'] = 0
    X.drop('thalassemia', 1, inplace=True)

    return X
