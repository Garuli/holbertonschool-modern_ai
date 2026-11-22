#!/usr/bin/env python3
"""Module that generates predictions from a trained classifier."""


def generate_predictions(clf, X):
    """Return the predicted class labels for the samples in X."""
    return clf.predict(X)
