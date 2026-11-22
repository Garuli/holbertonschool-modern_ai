#!/usr/bin/env python3
"""Module that plots a correlation heatmap of numeric features."""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """Annotated coolwarm heatmap of numeric feature correlations."""
    plt.figure(figsize=(6, 5))
    corr = df.select_dtypes(include='number').corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()
