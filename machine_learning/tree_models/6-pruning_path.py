#!/usr/bin/env python3
"""Module that retrieves the cost-complexity pruning path of a tree."""


def get_pruning_path(clf, X, y):
    """Return the effective ccp_alphas and the matching leaf impurities."""
    path = clf.cost_complexity_pruning_path(X, y)
    return path.ccp_alphas, path.impurities
