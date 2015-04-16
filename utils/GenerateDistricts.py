#!/usr/bin/python3

###################################################################
#
# File: GenerateDistricts.py
# Last Edit: 2015-04-08
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script combines the files in data/ocdIDs so we
# district information in either JSON or CSV format.
#
###################################################################

import os
import json
import csv
from datetime import datetime

YEAR = str(datetime.today().year)
OCDID_FILES = os.listdir('../data/ocdIDs/')
OUTFILE = YEAR + '_Districts' # file extension will be added
HEADERS = ['ocdID', 'name']
OUTPUT_JSON = False # otherwise CSV
PRETTY_PRINT = True # controls whitespace in JSON output
OUTFILENAME = OUTFILE + ('.json' if OUTPUT_JSON else '.csv')

def main():
    allOCDIDs = []
    for filename in OCDID_FILES:
        with open('data/ocdIDs/' + filename) as datafile:
            allOCDIDs += csv.reader(datafile)
    districts = []
    for ocdRecord in allOCDIDs:
        thisDistrict = {}
        thisDistrict['ocdID'] = ocdRecord[0]
        thisDistrict['name'] = ocdRecord[1]
        districts.append(thisDistrict)
    if OUTPUT_JSON:
        with open('data/' + OUTFILENAME, 'w') as datafile:
            if PRETTY_PRINT:
                json.dump(districts, datafile, sort_keys=True, 
                          indent=4, separators=(',', ': '))
            else:
                json.dump(districts, datafile)
    else: # output CSV
        with open('data/' + OUTFILENAME, 'w') as datafile:
            writer = csv.DictWriter(datafile, quoting=csv.QUOTE_ALL, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(districts)

if __name__=='__main__':
    main()
