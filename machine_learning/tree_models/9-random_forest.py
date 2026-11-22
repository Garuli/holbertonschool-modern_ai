#!/usr/bin/env python3
"""Module that creates a random forest classifier."""
from sklearn import ensemble


def random_forest(n_estimators, random_state):
    """Create an untrained RandomForestClassifier."""
    return ensemble.RandomForestClassifier(n_estimators=n_estimators,
                                           random_state=random_state)
