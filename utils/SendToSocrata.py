#!/usr/bin/python3

####################################################################################
#
# File: SendDataToSocrata.py
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script reads the files made by the Generate*.py scripts and
# sends their data to CFB Brigade Data Portal on Socrata using their API.
# Configuration parameters are read from 'config.ini'.
# Socrata's docs:
# http://dev.socrata.com/docs/endpoints.html
# Our data portal:
# https://brigades.opendatanetwork.com/catalog?Brigade_Group=Code%20for%20Birmingham
#
#####################################################################################

import os
import json
import requests
import sys
import hashlib
from configparser import ConfigParser
from requests.auth import HTTPBasicAuth
from requests.exceptions import Timeout

def main():
    # First read the config file.
    global config
    config = ConfigParser()
    config.read('config.ini')
    PRETTY_PRINT = config.get('SEND_TO_SOCRATA', 'PRETTY_PRINT')
    PARTIES_ID = config.get('SEND_TO_SOCRATA', 'PARTIES_ID')
    DISTRICTS_ID = config.get('SEND_TO_SOCRATA', 'DISTRICTS_ID')
    TRANSACTEES_ID = config.get('SEND_TO_SOCRATA', 'TRANSACTEES_ID')
    TRANSACTIONS_ID = config.get('SEND_TO_SOCRATA', 'TRANSACTIONS_ID')
    datasets = [PARTIES_ID, TRANSACTEES_ID, TRANSACTIONS_ID, DISTRICTS_ID]
    if sum(len(var) for var in datasets) == 0:
        print('>> Error: You must specify at least one dataset ID in the config file')
        sys.exit(1)
    DATA_DIR = config.get('SEND_TO_SOCRATA', 'DATA_DIR')
    PARTIES_FILE = config.get('GENERATE_PARTIES', 'OUTFILE')
    DISTRICTS_FILE = config.get('GENERATE_DISTRICTS', 'OUTFILE')
    TRANSACTEES_FILE = config.get('GENERATE_TRANSACTEES', 'OUTFILE')
    TRANSACTIONS_FILE = config.get('GENERATE_TRANSACTIONS', 'OUTFILE')
    HASHES_FILE = config.get('SEND_TO_SOCRATA', 'HASHES_FILE')
    # Check if the contents of each file have changed since the last run using MD5 hashes.
    oldHashes = {}
    try:
        with open(DATA_DIR + HASHES_FILE) as f:
            oldHashes = json.load(f)
    except FileNotFoundError:
        pass
    newHashes = {}
    hasher = hashlib.md5()
    filenames = [PARTIES_FILE, DISTRICTS_FILE, TRANSACTEES_FILE, TRANSACTIONS_FILE]
    for filename in filenames:
        try:
            with open(DATA_DIR + filename, 'rb') as f:
                hasher.update(f.read())
                newHashes[filename] = hasher.digest()
        except FileNotFoundError:
            print('>> Error: ' + filename + ' not found. Run the appropriate Generate script first.')
            sys.exit(2)
    # Send the data to Socrata for any files that have changed.
    if PARTIES_FILE not in oldHashes or newHashes[PARTIES_FILE] != oldHashes[PARTIES_FILE]:
        sendData(DATA_DIR + PARTIES_FILE, PARTIES_ID)
    if DISTRICTS_FILE not in oldHashes or newHashes[DISTRICTS_FILE] != oldHashes[DISTRICTS_FILE]:
        sendData(DATA_DIR + DISTRICTS_FILE, DISTRICTS_ID)
    if TRANSACTEES_FILE not in oldHashes or newHashes[TRANSACTEES_FILE] != oldHashes[TRANSACTEES_FILE]:
        sendData(DATA_DIR + TRANSACTEES_FILE, TRANSACTEES_ID)
    if TRANSACTIONS_FILE not in oldHashes or newHashes[TRANSACTIONS_FILE] != oldHashes[TRANSACTIONS_FILE]:
        sendData(DATA_DIR + TRANSACTIONS_FILE, TRANSACTIONS_ID)
    # Update the hashes for next time.
    with open(DATA_DIR + HASHES_FILE, 'w') as f:
        if PRETTY_PRINT:
            json.dump(newHashes, f, sort_keys=True,
                      indent=4, separators=(',', ': '))
        else:
            json.dump(newHashes, f)

# sends the data in the specified file to the specified resource
# returns boolean success
def sendData(filepath, resourceID):
    global config
    API_DOMAIN = config.get('SEND_TO_SOCRATA', 'API_DOMAIN')
    APP_KEY = config.get('SEND_TO_SOCRATA', 'APP_KEY')
    USERNAME = config.get('SEND_TO_SOCRATA', 'USERNAME')
    PASSWORD = config.get('SEND_TO_SOCRATA', 'PASSWORD')
    if len(APP_KEY) == 0 or len(USERNAME) == 0 or len(PASSWORD) == 0 or len(API_DOMAIN) == 0:
        print('>> Error: You must specify the Socrata domain, App Key, username, and password in the config file')
        sys.exit(1)
    if len(resourceID) == 0:
        return True # assume the user intended not to send this dataset
    if not os.path.isfile(filepath):
        print('>> Error: ' + filepath + ' not found. Run the appropriate Generate script.')
        return False
    with open(filepath) as f:
        data = json.load(f)
        print('>> Loaded ' + str(len(data)) + ' records from ' + filepath)
        try:
            headers = {
               'X-App-Token': APP_KEY
            }
            r = requests.post(API_DOMAIN + '/resource/' + resourceID + '.json', data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(USERNAME, PASSWORD))
            response = r.json()
            print('>> Number of errors = ' + str(response['Errors']))
            print('>> Rows deleted  = ' + str(response['Rows Deleted']))
            print('>> Rows updated = ' + str(response['Rows Updated']))
            print('>> Rows created = ' + str(response['Rows Created']))
        except Timeout as e:
            print(e)

if __name__=='__main__':
    main()
