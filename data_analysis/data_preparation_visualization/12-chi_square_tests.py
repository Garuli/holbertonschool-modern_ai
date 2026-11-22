#!/usr/bin/env python3
"""Module that runs chi-square tests between features and Churn."""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Return {feature: p_value} for each categorical feature vs Churn."""
    results = {}
    for col in df.select_dtypes(include='object').columns:
        if col == 'Churn':
            continue
        table = pd.crosstab(df[col], df['Churn'])
        results[col] = stats.chi2_contingency(table)[1]
    return results
