#!/usr/bin/env python3
"""Module that drops the customerID column."""


def drop_customerID(df):
    """Return the DataFrame without the customerID column."""
    return df.drop(columns=['customerID'])
