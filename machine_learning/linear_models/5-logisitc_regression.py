#!/usr/bin/env python3
"""Module that creates a logistic regression model."""
from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Create an untrained LogisticRegression model for classification."""
    return linear_model.LogisticRegression(random_state=random_state)
