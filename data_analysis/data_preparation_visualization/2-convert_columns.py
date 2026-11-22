#!/usr/bin/env python3
"""Module that converts column types in the churn dataset."""
import pandas as pd


def convert_columns(df):
    """Make TotalCharges numeric and map SeniorCitizen 0/1 to No/Yes."""
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
    return df
