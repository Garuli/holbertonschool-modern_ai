#!/usr/bin/env python3
"""Module that prints the text structure of a trained decision tree."""
from sklearn import tree


def draw(clf, feature_names, class_names):
    """Print the decision rules of a trained decision tree classifier."""
    print(tree.export_text(clf,
                           feature_names=list(feature_names),
                           class_names=list(class_names)))
