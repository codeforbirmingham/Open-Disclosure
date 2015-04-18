#!/usr/bin/python3

###################################################################
#
# File: GenerateDistricts.py
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script combines the files in data/ocdIDs to output
# district information in JSON format.
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
    OUTFILE = config.get('GENERATE_DISTRICTS', 'OUTFILE')
    PRETTY_PRINT = config.getboolean('GENERATE_DISTRICTS', 'PRETTY_PRINT')
    allOCDIDs = []
    for filename in OCDID_FILES:
        with open(OCDID_DIR + filename) as datafile:
            print('>> Loading data from ' + filename)
            allOCDIDs += csv.reader(datafile)
    districts = []
    for ocdRecord in allOCDIDs:
        thisDistrict = {}
        thisDistrict['ocdID'] = ocdRecord[0]
        thisDistrict['name'] = ocdRecord[1]
        districts.append(thisDistrict)
    print('>> Writing ' + str(len(districts)) + ' records to ' + OUTFILE)
    with open(DATA_DIR + OUTFILE, 'w') as datafile:
        if PRETTY_PRINT:
            json.dump(districts, datafile, sort_keys=True, 
                      indent=4, separators=(',', ': '))
        else:
            json.dump(districts, datafile)

if __name__=='__main__':
    main()
