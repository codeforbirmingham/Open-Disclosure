#!/usr/bin/python3

__author__ = 'mleeds95'

'''
This script reads filenames from 'config.ini' and turns any lists into strings.
'''

import sys
import json
from configparser import ConfigParser

def flatten(data):
    # Assume the data is a list of dicts.
    # Convert lists to strings.
    for record in data:
        for key in record:
            if isinstance(record[key], list):
                record[key] = str(record[key])
    return data

def main():
    config = ConfigParser()
    config.read('config.ini')
    DATA_DIR = config.get('GENERATE_TRANSACTIONS', 'DATA_DIR')
    PRETTY_PRINT = config.getboolean('GENERATE_TRANSACTIONS', 'PRETTY_PRINT')
    TRANSACTEES_FILE = config.get('GENERATE_TRANSACTEES', 'OUTFILE')
    TRANSACTIONS_FILE = config.get('GENERATE_TRANSACTIONS', 'OUTFILE')
    for filename in (TRANSACTEES_FILE, TRANSACTIONS_FILE):
        try:
            with open(DATA_DIR + filename) as datafile:
                structuredData = json.load(datafile)
        except FileNotFoundError:
            print('>> ' + filename + ' not found! You should run the appropriate Generate script first.')
            sys.exit(1)
        print('>> Flattening ' + str(len(structuredData)) + ' records from ' + filename + '...', end='')
        flatData = flatten(structuredData)
        print('Done!')
        with open(DATA_DIR + filename, 'w') as outfile:
            if PRETTY_PRINT:
                json.dump(flatData, outfile, sort_keys=True,
                          indent=4, separators=(',', ': '))
            else:
                json.dump(flatData, outfile)

if __name__ == '__main__':
    main()
