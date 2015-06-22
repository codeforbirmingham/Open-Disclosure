#!/usr/bin/python3

###################################################################
#
# File: GenerateParties.py
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script reads the data files from alabamavotes.gov
# and finds all the unique PACs & Candidates (by OrgID).
# It also reads the Party information from that site, and
# cross-references it with the existing data. 
# This data can then be expanded by CallCivicInfoAPI.py
# Configuration parameters are read from 'config.ini'.
#
###################################################################

import json
import csv
import re
from datetime import datetime
from configparser import ConfigParser

def main():
    # First read the config file.
    config = ConfigParser()
    config.read('config.ini')
    DATA_DIR = config.get('GENERATE_PARTIES', 'DATA_DIR')
    PARTYINFO = config.get('PARTY_FETCHER', 'destination_file')
    DATAFILES = json.loads(config.get('GENERATE_PARTIES', 'DATAFILES'))
    OUTFILE = config.get('GENERATE_PARTIES', 'OUTFILE')
    PRETTY_PRINT = config.getboolean('GENERATE_PARTIES', 'PRETTY_PRINT')
    global allParties
    allParties = [] # all PACs and Candidates
    global allOrgIDs
    allOrgIDs = [] # used to ensure we don't have duplicates
    # start by finding all unique organizations (by id) and adding them to allParties
    for filename in DATAFILES:
        with open(DATA_DIR + filename, 'r', errors='ignore', newline='') as csvfile:
            print('>> Loading data from ' + filename)
            findUniqueOrgs(csv.DictReader(csvfile))
    # add the info we have on each candidate from the Parties file
    with open(DATA_DIR + PARTYINFO) as datafile:
        numModified = addPartyInfo(csv.DictReader(datafile))
    print('>> Modified ' + str(numModified) + ' party records with additional info.')
    # Add OCD IDs for any districts we can identify.
    numModified = addDistrictIDs()
    print('>> Added District IDs to ' + str(numModified) + ' records.')
    print('>> Writing ' + str(len(allParties)) + ' records to ' + OUTFILE)
    with open(DATA_DIR + OUTFILE, 'w') as datafile:
        if PRETTY_PRINT:
            json.dump(allParties, datafile, sort_keys=True, 
                      indent=4, separators=(',', ': '))
        else:
            json.dump(allParties, datafile)

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
            thisOrg['id'] = record['OrgID']
            thisOrg['API_status'] = '' # this field will be used by CallCivicInfo.py
            if record['CommitteeType'] == 'Political Action Committee':
                thisOrg['type'] = 'PAC'
                rawName = record['CommitteeName']
                thisOrg['name'] = rawName.title().replace('Pac', 'PAC').replace('"', '').strip()
                if thisOrg['name'][-3:].upper() == 'PAC': 
                    thisOrg['name'] = thisOrg['name'][:-3] + 'PAC'
            elif record['CommitteeType'] == 'Principal Campaign Committee':
                thisOrg['type'] = 'Candidate'
                rawName = record['CandidateName']
                thisOrg['name'] = rawName.title().replace('Ii', 'II').replace('Iii', 'III').replace('IIi', 'III').replace('"', '').strip()
            else:
                print('>> Error: Unknown group type: ' + record['CommitteeType'])
            allParties.append(thisOrg)

def addPartyInfo(records):
    global allParties
    numModified = 0
    # iterate over the records and add the info to allParties
    for record in records:
        # if the ID is in the data, add to it
        for party in allParties:
            if party['id'] == record['CommitteeID']:
                numModified += 1
                party['party'] = record['Party']
                party['office'] = record['Office']
                if len(record['District']) > 0: 
                    party['district'] = record['District']
                if len(record['Place']) > 0:
                    party['place'] = record['Place'].strip()
                party['status'] = record['CommitteeStatus']
                break
    return numModified

def addDistrictIDs():
    global allParties
    numModified = 0
    # Add OCD IDs for anyone in the state legislature.
    districtPattern = r'^(HOUSE|SENATE) DISTRICT \d+$'
    for party in allParties:
        if 'district' in party and re.match(districtPattern, party['district']) != None:
            print(party['district'])
            districtID = 'ocd-division/country:us/state:al/sld'
            districtID += ('u' if 'SENATE' in party['district'] else 'l')
            districtID += ':' + party['district'].split(' ')[-1]
            party['ocdID'] = districtID
            numModified += 1
    return numModified

if __name__=='__main__':
    main()
