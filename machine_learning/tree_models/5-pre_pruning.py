#!/usr/bin/env python3
"""Module that finds the best pre-pruning parameters with grid search."""
from sklearn import model_selection


def prepruning(X, y, clf):
    """Grid search pre-pruning hyperparameters and return the best ones."""
    param_grid = {
        "criterion": ["gini", "entropy"],
        "max_depth": list(range(2, 5)),
        "min_samples_leaf": list(range(2, 5)),
        "min_samples_split": list(range(2, 5)),
    }
    grid = model_selection.GridSearchCV(clf, param_grid)
    grid.fit(X, y)
    return grid.best_params_
