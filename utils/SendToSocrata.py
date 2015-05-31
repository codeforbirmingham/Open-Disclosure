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
from configparser import ConfigParser
from requests.auth import HTTPBasicAuth
from requests.exceptions import Timeout

def main():
    # First read the config file.
    global config
    config = ConfigParser()
    config.read('config.ini')
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
    print('>> Sending data')
    sendData(DATA_DIR + PARTIES_FILE, PARTIES_ID)
    sendData(DATA_DIR + DISTRICTS_FILE, DISTRICTS_ID)
    sendData(DATA_DIR + TRANSACTEES_FILE, TRANSACTEES_ID)
    sendData(DATA_DIR + TRANSACTIONS_FILE, TRANSACTIONS_ID)

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
        return True
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
