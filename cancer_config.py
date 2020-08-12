# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:29:59 2020

@author: rkbra
"""

MODEL_NAME = "./models/cancer.pickle"

TARGET = "diagnosis"

FEATURES = [
    "radius_mean",
    "texture_mean",
    "smoothness_mean",
    "compactness_mean",
    "concavity_mean",
    "concave points_mean",
    "symmetry_mean",
    "fractal_dimension_mean",
    "radius_se",
    "texture_se",
    "smoothness_se",
    "compactness_se",
    "concavity_se",
    "concave points_se",
    "symmetry_se",
    "fractal_dimension_se",
    "radius_worst",
    "texture_worst",
    "smoothness_worst",
    "compactness_worst",
    "concavity_worst",
    "concave points_worst",
    "symmetry_worst",
    "fractal_dimension_worst",
]

FORM_INPUT = [
    {
        "label": "Mean of distances of the cell nucleus from center to points on the perimeter",
        "input": "radius_mean",
        "type": "text",
    },
    {
        "label": "Standard Deviation of gray-scale values of the cell nucleus",
        "input": "texture_mean",
        "type": "text",
    },
    {
        "label": "Mean of local variation in radius lengths of the cell nucleus",
        "input": "smoothness_mean",
        "type": "text",
    },
    {
        "label": "Mean of perimeter^2 / area - 1.0",
        "input": "compactness_mean",
        "type": "text",
    },
    {
        "label": "Mean of severity of concave portions of the contour",
        "input": "concavity_mean",
        "type": "text",
    },
    {
        "label": "Mean for number of concave portions of the contour",
        "input": "concave_points_mean",
        "type": "text",
    },
    {"label": "Symmetry Mean", "input": "symmetry_mean", "type": "text"},
    {
        "label": "Mean for 'coastline approximation' - 1",
        "input": "fractal_dimension_mean",
        "type": "text",
    },
    {
        "label": "Standard error for the mean of distances from center to points on the perimeter",
        "input": "radius_se",
        "type": "text",
    },
    {
        "label": "Standard error for standard deviation of gray-scale values",
        "input": "texture_se",
        "type": "text",
    },
    {
        "label": "Standard error for local variation in radius lengths",
        "input": "smoothness_se",
        "type": "text",
    },
    {
        "label": "standard error for perimeter^2 / area - 1.0",
        "input": "compactness_se",
        "type": "text",
    },
    {
        "label": "Standard error for severity of concave portions of the contour",
        "input": "concavity_se",
        "type": "text",
    },
    {
        "label": "Standard error for number of concave portions of the contour",
        "input": "concave_points_se",
        "type": "text",
    },
    {"label": "Standar Error for Symmetry", "input": "symmetry_se", "type": "text"},
    {
        "label": "Standard Error for 'coastline approximation' - 1",
        "input": "fractal_dimension_se",
        "type": "text",
    },
    {
        "label": 'Worst or Largest Mean value for mean of distances from center to points on the perimeter',
        "input": "radius_worst",
        "type": "text",
    },
    {
        "label": '"worst" or largest mean value for standard deviation of gray-scale values',
        "input": "texture_worst",
        "type": "text",
    },
    {
        "label": '"worst" or largest mean value for local variation in radius lengths',
        "input": "smoothness_worst",
        "type": "text",
    },
    {
        "label": "Worst or largest mean value for for perimeter^2 / area - 1.0",
        "input": "compactness_worst",
        "type": "text",
    },
    {
        "label": '"worst" or largest mean value for severity of concave portions of the contour',
        "input": "concavity_worst",
        "type": "text",
    },
    {
        "label": '"worst" or largest mean value for number of concave portions of the contour',
        "input": "concave_points_worst",
        "type": "text",
    },
    {
        "label": '"worst" or largest mean value for symmetry of the cell nucleus',
        "input": "symmetry_worst",
        "type": "text",
    },
    {
        "label": '"worst" or largest mean value for "coastline approximation" - 1',
        "input": "fractal_dimension_worst",
        "type": "text",
    },
]
