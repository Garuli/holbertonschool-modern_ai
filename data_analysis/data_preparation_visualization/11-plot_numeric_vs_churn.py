#!/usr/bin/env python3
"""Module that compares a numeric feature distribution by churn."""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """Histograms of a numeric column for Churn=No and Churn=Yes."""
    plt.figure(figsize=(12, 8))
    no = df[df['Churn'] == 'No'][col]
    yes = df[df['Churn'] == 'Yes'][col]
    plt.hist([no, yes], bins=30, label=['No', 'Yes'])
    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)
    plt.legend(title='Churn')
    plt.show()
