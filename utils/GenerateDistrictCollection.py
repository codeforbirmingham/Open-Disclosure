#!/usr/bin/python3

###################################################################
#
# File: GenerateDistrictCollection.py
# Last Edit: 2015-02-05
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: This script combines the files in data/ocdIDs so we
# district information in a format that's importable into mongoDB.
#
###################################################################

import json
import os
import csv

OCDID_FILES = os.listdir('../data/ocdIDs/')
OUTFILE = '2014_DistrictCollection.json'

def main():
    allOCDIDs = []
    for filename in OCDID_FILES:
        with open('../data/ocdIDs/' + filename) as datafile:
            allOCDIDs += csv.reader(datafile)
    districts = []
    for ocdRecord in allOCDIDs:
        thisDistrict = {}
        thisDistrict['ocdID'] = ocdRecord[0]
        thisDistrict['name'] = ocdRecord[1]
        districts.append(thisDistrict)
    with open('../data/import/' + OUTFILE, 'w') as datafile:
        json.dump(districts, datafile, sort_keys=True, 
                  indent=4, separators=(',', ': '))

if __name__=='__main__':
    main()
