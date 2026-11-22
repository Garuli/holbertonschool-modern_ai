#!/usr/bin/env python3
"""Module that plots the churn class distribution."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Bar plot of Churn value counts (No: skyblue, Yes: salmon)."""
    plt.figure(figsize=(12, 8))
    counts = df['Churn'].value_counts()
    colors = ['skyblue' if v == 'No' else 'salmon' for v in counts.index]
    plt.bar(counts.index, counts.values, color=colors)
    plt.title("Churn Distribution")
    plt.ylabel("Count")
    plt.show()
