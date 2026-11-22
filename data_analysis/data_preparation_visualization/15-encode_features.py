#!/usr/bin/env python3
"""Module that encodes features for modeling."""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode target, binary, one-hot and TenureGroup columns."""
    df = df.copy()
    churn_le = preprocessing.LabelEncoder()
    df['Churn'] = churn_le.fit_transform(df['Churn'])

    binary_oe = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])
    for col in ['Partner', 'Dependents', 'PaperlessBilling',
                'SeniorCitizen']:
        df[col] = binary_oe.fit_transform(df[[col]]).astype(int).ravel()

    tenure_oe = preprocessing.OrdinalEncoder()
    df['TenureGroup'] = tenure_oe.fit_transform(
        df[['TenureGroup']].astype(str)).astype(int).ravel()

    df = pd.get_dummies(df, columns=['Contract', 'PaymentMethod'],
                        drop_first=True, dtype=int)
    return df, churn_le, binary_oe, tenure_oe
