#!/usr/bin/env python3
"""Module that standardizes numeric columns."""
from sklearn import preprocessing


def scale_numeric(df):
    """Scale MonthlyCharges and TotalCharges to mean 0 and std 1."""
    df = df.copy()
    cols = ['MonthlyCharges', 'TotalCharges']
    df[cols] = preprocessing.StandardScaler().fit_transform(df[cols])
    return df
