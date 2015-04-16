#!/usr/bin/python3

###################################################################
#
# File: GenerateDistricts.py
# Last Edit: 2015-04-16
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script combines the files in data/ocdIDs so we
# district information in either JSON or CSV format.
# Configuration parameters are read from 'config.ini'.
#
###################################################################

import os
import json
import csv
from datetime import datetime
from configparser import ConfigParser

def main():
    # First read the config file.
    config = ConfigParser()
    config.read('config.ini')
    DATA_DIR = config.get('GENERATE_DISTRICTS', 'DATA_DIR')
    OCDID_DIR = config.get('GENERATE_DISTRICTS', 'OCDID_DIR')
    OCDID_FILES = os.listdir(OCDID_DIR)
    OUTPUT_JSON = config.getboolean('GENERATE_DISTRICTS', 'OUTPUT_JSON')
    OUTFILE = config.get('GENERATE_DISTRICTS', 'OUTFILE') + ('.json' if OUTPUT_JSON else '.csv')
    HEADERS = json.loads(config.get('GENERATE_DISTRICTS', 'HEADERS'))
    PRETTY_PRINT = config.getboolean('GENERATE_DISTRICTS', 'PRETTY_PRINT')
    allOCDIDs = []
    for filename in OCDID_FILES:
        with open(OCDID_DIR + filename) as datafile:
            allOCDIDs += csv.reader(datafile)
    districts = []
    for ocdRecord in allOCDIDs:
        thisDistrict = {}
        thisDistrict['ocdID'] = ocdRecord[0]
        thisDistrict['name'] = ocdRecord[1]
        districts.append(thisDistrict)
    if OUTPUT_JSON:
        with open(DATA_DIR + OUTFILE, 'w') as datafile:
            if PRETTY_PRINT:
                json.dump(districts, datafile, sort_keys=True, 
                          indent=4, separators=(',', ': '))
            else:
                json.dump(districts, datafile)
    else: # output CSV
        with open(DATA_DIR + OUTFILE, 'w') as datafile:
            writer = csv.DictWriter(datafile, quoting=csv.QUOTE_ALL, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(districts)

if __name__=='__main__':
    main()
