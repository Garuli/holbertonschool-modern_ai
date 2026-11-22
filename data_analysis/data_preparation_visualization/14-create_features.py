#!/usr/bin/env python3
"""Module that engineers NumServices and TenureGroup features."""
import pandas as pd


def create_features(df):
    """Add NumServices and TenureGroup, then drop their source columns."""
    df = df.copy()
    services = ['MultipleLines', 'InternetService', 'OnlineSecurity',
                'OnlineBackup', 'DeviceProtection', 'TechSupport',
                'StreamingTV', 'StreamingMovies']
    internet = df['InternetService'].isin(['DSL', 'Fiber optic'])
    others = (df[services].drop(columns=['InternetService']) == 'Yes')
    df['NumServices'] = others.sum(axis=1) + internet.astype(int)
    df['TenureGroup'] = pd.cut(df['tenure'],
                               bins=[0, 12, 24, 48, 60, float('inf')],
                               labels=['0-12', '13-24', '25-48',
                                       '49-60', '60+'])
    df = df.drop(columns=services + ['tenure'])
    return df
