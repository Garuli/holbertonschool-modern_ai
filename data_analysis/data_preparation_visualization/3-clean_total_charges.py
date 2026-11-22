#!/usr/bin/env python3
"""Module that handles missing values in TotalCharges."""


def clean_total_charges(df, method='drop'):
    """Drop, median-fill or impute missing TotalCharges values."""
    df = df.copy()
    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])
    elif method == 'median':
        median = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median)
    elif method == 'impute':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['MonthlyCharges'] * df['tenure'])
    return df
