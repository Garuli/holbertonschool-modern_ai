#!/usr/bin/env python3
"""Module that plots the churn rate per category."""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """Bar plot of the churn rate (Yes proportion) for each category."""
    plt.figure(figsize=(12, 8))
    rate = df.groupby(col)['Churn'].apply(lambda s: (s == 'Yes').mean())
    plt.bar(rate.index.astype(str), rate.values)
    plt.title(f"Churn Rate by {col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)
    plt.show()
