#!/usr/bin/env python3
"""Module that computes feature importances of a random forest."""
import numpy as np


def feature_importance(rf):
    """Return importances and indices sorted from least to most important."""
    importances = rf.feature_importances_
    indices = np.argsort(importances)
    return importances, indices
