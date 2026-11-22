#!/usr/bin/env python3
"""Module that creates a Ridge regression model."""
from sklearn import linear_model


def ridge_regression(random_state):
    """Create an untrained Ridge regression model with L2 regularization."""
    return linear_model.Ridge(random_state=random_state)
