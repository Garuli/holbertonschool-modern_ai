#!/usr/bin/env python3
"""Module that runs Welch's t-tests on numeric features by Churn."""
from scipy import stats


def ttest_numeric(df):
    """Return {feature: p_value} comparing Churn=Yes vs Churn=No."""
    results = {}
    for col in df.select_dtypes(include='number').columns:
        yes = df[df['Churn'] == 'Yes'][col]
        no = df[df['Churn'] == 'No'][col]
        results[col] = stats.ttest_ind(yes, no, equal_var=False).pvalue
    return results
