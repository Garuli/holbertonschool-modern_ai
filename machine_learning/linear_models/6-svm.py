#!/usr/bin/env python3
"""Module that creates SVM classifiers with different kernels."""
from sklearn import svm


def get_SVM_model(name, random_state):
    """Create an untrained SVC with a linear, poly or rbf kernel."""
    return svm.SVC(kernel=name, random_state=random_state)
