#!/usr/bin/env python3
"""Module that creates a Lasso regression model."""
from sklearn import linear_model


def lasso_regression(random_state):
    """Create an untrained Lasso regression model with L1 regularization."""
    return linear_model.Lasso(random_state=random_state)
