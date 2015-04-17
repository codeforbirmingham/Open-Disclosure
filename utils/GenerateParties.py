#!/usr/bin/python3

###################################################################
#
# File: GenerateParties.py
# Last Edit: 2015-04-16
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script reads the data files from alabamavotes.gov
# and finds all the unique PACs & Candidates (by OrgID).
# It also reads the Party information from that site, and
# cross-references it with the existing data. 
# It can output Party data either in JSON or CSV format.
# This data can then be expanded by CallCivicInfoAPI.py
# Configuration parameters are read from 'config.ini'.
#
###################################################################

import json
import csv
from datetime import datetime
from configparser import ConfigParser

def main():
    # First read the config file.
    config = ConfigParser()
    config.read('config.ini')
    DATA_DIR = config.get('GENERATE_PARTIES', 'DATA_DIR')
    PARTYINFO = config.get('PARTY_FETCHER', 'destination_file')
    DATAFILES = json.loads(config.get('GENERATE_PARTIES', 'DATAFILES'))
    HEADERS = json.loads(config.get('GENERATE_PARTIES', 'HEADERS'))
    OUTPUT_JSON = config.getboolean('GENERATE_PARTIES', 'OUTPUT_JSON')
    OUTFILE = config.get('GENERATE_PARTIES', 'OUTFILE') + ('.json' if OUTPUT_JSON else '.csv')
    PRETTY_PRINT = config.getboolean('GENERATE_PARTIES', 'PRETTY_PRINT')
    global allParties
    allParties = [] # all PACs and Candidates
    global allOrgIDs
    allOrgIDs = [] # used to ensure we don't have duplicates
    # start by finding all unique organizations (by id) and adding them to allParties
    for filename in DATAFILES:
        with open(DATA_DIR + filename, 'r', errors='replace', newline='') as csvfile:
            findUniqueOrgs(csv.DictReader(csvfile))
    print('>> Found ' + str(len(allParties)) + ' unique parties.')
    # add the info we have on each candidate from the Parties file
    with open(DATA_DIR + PARTYINFO) as datafile:
        numModified = addPartyInfo(csv.DictReader(datafile))
    print('>> Modified ' + str(numModified) + ' party records with additional info.')
    print('>> Writing party data to ' + OUTFILE + '.')
    if OUTPUT_JSON:
        with open(DATA_DIR + OUTFILE, 'w') as datafile:
            if PRETTY_PRINT:
                json.dump(allParties, datafile, sort_keys=True, 
                          indent=4, separators=(',', ': '))
            else:
                json.dump(allParties, datafile)
    else: # output CSV
        with open(DATA_DIR + OUTFILE, 'w', newline='') as datafile:
            writer = csv.DictWriter(datafile, quoting=csv.QUOTE_ALL, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(allParties)

def findUniqueOrgs(records):
    global allParties
    global allOrgIDs
    numParties = 0 
    # iterate over the records looking for new information
    for record in records:
        # if it's a new OrgID, gather the info
        if record['OrgID'] not in allOrgIDs:
            numParties += 1
            allOrgIDs.append(record['OrgID'])
            thisOrg = {} 
            thisOrg['_id'] = record['OrgID']
            thisOrg['_API_status'] = '' # this field will be used by CallCivicInfo.py
            if record['CommitteeType'] == 'Political Action Committee':
                thisOrg['type'] = 'PAC'
                rawName = record['CommitteeName']
                thisOrg['name'] = rawName.title().replace('Pac', 'PAC').replace('"', '').strip()
            elif record['CommitteeType'] == 'Principal Campaign Committee':
                thisOrg['type'] = 'Candidate'
                rawName = record['CandidateName']
                thisOrg['name'] = rawName.title().replace('Ii', 'II').replace('Iii', 'III').replace('"', '').strip()
            else:
                print('>> Error: Unknown group type: ' + record['CommitteeType'])
            allParties.append(thisOrg)

def addPartyInfo(records):
    numModified = 0
    # iterate over the records and add the info to allParties
    for record in records:
        # if the ID is in the data, add to it
        for party in allParties:
            if party['_id'] == record['CommitteeID']:
                numModified += 1
                party['name'] = record['CandidateName']
                party['party'] = record['Party']
                party['office'] = record['Office']
                if len(record['District']) > 0: 
                    party['district'] = record['District']
                if len(record['Place']) > 0:
                    party['place'] = record['Place']
                party['status'] = record['CommitteeStatus']
                break
    return numModified

if __name__=='__main__':
    main()