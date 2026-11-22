#!/usr/bin/env python3
"""Module that trains a tree-based classifier."""


def train_tree(clf, X, y):
    """Fit the given classifier on features X and labels y."""
    clf.fit(X, y)
