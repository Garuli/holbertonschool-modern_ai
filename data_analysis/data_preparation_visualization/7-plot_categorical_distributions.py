#!/usr/bin/env python3
"""Module that plots categorical feature distributions."""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Grid of bar plots with the value counts of categorical columns."""
    if columns_to_plot is None:
        cols = [c for c in df.select_dtypes(include='object').columns
                if c != 'Churn']
    else:
        cols = list(columns_to_plot)
    n_cols, n_rows = 3, (len(cols) + 2) // 3
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
    axes = axes.flatten()

    for ax, col in zip(axes, cols):
        counts = df[col].value_counts()
        ax.bar(counts.index.astype(str), counts.values)
        ax.set_title(col)
        ax.tick_params(axis='x', rotation=45)
    for ax in axes[len(cols):]:
        fig.delaxes(ax)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
