#!/usr/bin/env python3

##### Imports #####
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
import api_access

"""
##### Classes #####
class jsonWrangler():

    def __init__(self, file):
    

##### Functions #####
def json2var():

"""
def wrangle(fileList):
    data = {}
    for dataset in fileList:
        for entry in totalAB:
                date=entry['date']
                metric=entry['metric']
                stratum=entry['stratum']
                value=entry['metric_value']
                if date not in data:
                    data[date]={}
                data[date][metric]=value
                data[date]["stratum"]=stratum
    return data

def cleanName(fileName):
    rawName = fileName
    partsList = rawName.rsplit("_", 1)
    name = partsList[-1].removesuffix(".json")
    return name

def parse_date(datestring):
    """ Convert a date string into a pandas datetime object """
    return pd.to_datetime(datestring, format="%Y-%m-%d")

##### Variables #####
abFiles = ["data/antibiotics_consumption_totalDID.json", "data/antibiotics_consumption_totalAware.json", "data/antibiotics_consumption_awareAccess", "data/antibiotics_consumption_awareReserve.json", "data/antibiotics_consumption_awareWatch.json", "data/antibiotics_consumption_primaryAware", "data/antibiotics_consumption_primaryDID","data/antibiotics_consumption_primaryCareRateByMonth", "data/antibiotics_consumption_secondaryDID"]

##### Script #####

# First, we need to load all the json files and assign them to variables.
for file in abFiles:    
    print(cleanName(file))

"""
with open("data/antibiotics_consumption_totalDID.json", "rt") as INFILE:
    totalAB=json.load(INFILE)
with open("data/antibiotics_consumption_totalAware.json", "rt") as INFILE:
    totalABAware=json.load(INFILE)
"""
