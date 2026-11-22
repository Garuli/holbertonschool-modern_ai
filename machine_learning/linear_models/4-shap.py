#!/usr/bin/env python3
"""Module that builds a SHAP explainer and computes SHAP values."""
import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Create a SHAP explainer on X_train and compute values for X_test."""
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
