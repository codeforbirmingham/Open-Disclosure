#!/usr/bin/python

####################################################################################
#
# File: SendDataToSocrata.py
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script reads the files made by the Generate*.py scripts and
# sends their data to CFB Brigade Data Portal on Socrata using their API and
# the sodapy library. Configuration parameters are read from 'config.ini'.
# Unfortunately it's Python 2 since sodapy requires that.
# Install sodapy with 'pip install sodapy'
# Socrata's docs:
# http://dev.socrata.com/docs/endpoints.html
# Our data portal:
# https://brigades.opendatanetwork.com/catalog?Brigade_Group=Code%20for%20Birmingham
#
#####################################################################################

import os
import json
import sys
from sodapy import Socrata
from ConfigParser import ConfigParser
from requests.exceptions import Timeout

def main():
    # First read the config file.
    config = ConfigParser()
    config.read('config.ini')
    API_DOMAIN = config.get('SEND_TO_SOCRATA', 'API_DOMAIN')
    APP_KEY = config.get('SEND_TO_SOCRATA', 'APP_KEY')
    USERNAME = config.get('SEND_TO_SOCRATA', 'USERNAME')
    PASSWORD = config.get('SEND_TO_SOCRATA', 'PASSWORD')
    if len(APP_KEY) == 0 or len(USERNAME) == 0 or len(PASSWORD) == 0 or len(API_DOMAIN) == 0:
        print '>> Error: You must specify the Socrata domain, App Key, username, and password in the config file'
        sys.exit(1)
    PARTIES_ID = config.get('SEND_TO_SOCRATA', 'PARTIES_ID')
    DISTRICTS_ID = config.get('SEND_TO_SOCRATA', 'DISTRICTS_ID')
    TRANSACTEES_ID = config.get('SEND_TO_SOCRATA', 'TRANSACTEES_ID')
    TRANSACTIONS_ID = config.get('SEND_TO_SOCRATA', 'TRANSACTIONS_ID')
    datasets = [PARTIES_ID, TRANSACTEES_ID, TRANSACTIONS_ID, DISTRICTS_ID]
    if sum(len(var) for var in datasets) == 0:
        print '>> Error: You must specify at least one dataset ID in the config file'
        sys.exit(1)
    DATA_DIR = config.get('SEND_TO_SOCRATA', 'DATA_DIR')
    PARTIES_FILE = config.get('GENERATE_PARTIES', 'OUTFILE')
    DISTRICTS_FILE = config.get('GENERATE_DISTRICTS', 'OUTFILE')
    TRANSACTEES_FILE = config.get('GENERATE_TRANSACTEES', 'OUTFILE')
    TRANSACTIONS_FILE = config.get('GENERATE_TRANSACTIONS', 'OUTFILE')
    # connect to Socrata
    print '>> Connecting to ' + API_DOMAIN + ' and authenticating'
    client = Socrata(API_DOMAIN, APP_KEY, username=USERNAME, password=PASSWORD)
    print '>> Sending data'
    sendData(client, DATA_DIR + PARTIES_FILE, PARTIES_ID)
    sendData(client, DATA_DIR + DISTRICTS_FILE, DISTRICTS_ID)
    sendData(client, DATA_DIR + TRANSACTEES_FILE, TRANSACTEES_ID)
    sendData(client, DATA_DIR + TRANSACTIONS_FILE, TRANSACTIONS_ID)
    print '>> Closing the connection'
    client.close()

# sends the data in the specified file to the specified resource
# returns boolean success
def sendData(client, filepath, resourceID):
    if len(resourceID) == 0: 
        return True
    if not os.path.isfile(filepath):
        print '>> Error: ' + filepath + ' not found. Run the appropriate Generate script.'
        return False
    with open(filepath) as f:
        allData = json.load(f)
        print '>> Loaded ' + str(len(allData)) + ' records from ' + filepath
        numErrors, numDeleted, numUpdated, numCreated = 0, 0, 0, 0
        for record in allData:
            try:
                response = client.upsert('/resource/' + resourceID + '.json', [record])
            except Timeout as e:
                print e 
                break
            numErrors += response['Errors']
            numDeleted += response['Rows Deleted']
            numUpdated += response['Rows Updated']
            numCreated += response['Rows Created']
        print '>> Number of errors = ' + str(numErrors)
        print '>> Rows deleted  = ' + str(numDeleted)
        print '>> Rows updated = ' + str(numUpdated)
        print '>> Rows created = ' + str(numCreated)
    if numErrors == 0:
        return True
    else:
        return False

if __name__=='__main__':
    main()
