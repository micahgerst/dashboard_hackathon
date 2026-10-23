#!/usr/bin/env python3

##### Imports #####
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
import api_access

##### Functions #####

def wrangle(fileList):
    """DOES NOT WORK ON PRIMARYMONTHLY"""
    data = {}
    for file in fileList:
        for entry in file:
            date=entry['date']
            metric=entry['metric']
            cleanmet=metric.rsplit("_", 1)[-1]
            value=entry['metric_value']
            if date not in data:
                data[date]={}
            data[date][cleanmet]=value
    return data

def parse_date(datestring):
    """ Convert a date string into a pandas datetime object """
    return pd.to_datetime(datestring, format="%Y-%m-%d")

def get_timeframe(data):
    dates=list(data.keys())
    dates.sort()
    startdate=parse_date(dates[0])
    enddate=parse_date(dates[-1])
    return [startdate, enddate]
