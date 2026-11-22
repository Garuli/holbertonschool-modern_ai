#!/usr/bin/env python3
"""Module that visualizes missing values in a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Scatter plot of missing values: rows on x-axis, columns on y-axis."""
    plt.figure(figsize=(12, 8))
    rows, cols = np.where(df.isnull())
    plt.scatter(rows, cols, marker='|')
    plt.yticks(range(len(df.columns)), df.columns)
    plt.title("Missingness Plot")
    plt.tight_layout()
    plt.show()
