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
import sys
from datetime import datetime
from configparser import ConfigParser

def main():
    # First read the config file.
    config = ConfigParser()
    config.read('config.ini')
    DATA_DIR = config.get('GENERATE_PARTIES', 'DATA_DIR')
    PARTYINFO = config.get('PARTY_FETCHER', 'destination_file')
    DISTRICTS_FILE = config.get('GENERATE_DISTRICTS', 'OUTFILE')
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
    # Load the OCD IDs so we know which ones are valid.
    global allDistricts
    try:
        with open(DATA_DIR + DISTRICTS_FILE) as f:
            allDistricts = json.load(f)
    except FileNotFoundError:
        print('>> Error: ' + DISTRICTS_FILE + ' not found! Run GenerateDistricts.py first.')
        sys.exit(1)
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
        found = False
        for party in allParties:
            if party['id'] == record['CommitteeID']:
                party['party'] = record['Party']
                party['office'] = record['Office']
                if len(record['District']) > 0: 
                    party['district'] = record['District']
                if len(record['Place']) > 0:
                    party['place'] = record['Place'].strip()
                party['status'] = record['CommitteeStatus']
                numModified += 1
                found = True
                break
        if not found:
            # it's a party with no submitted CFC data; add it anyway.
            newParty = {}
            newParty['id'] = record['CommitteeID']
            normalizedName = record['CandidateName'].split(',')[1].strip() + ' ' + record['CandidateName'].split(',')[0]
            normalizedName = normalizedName.title().replace('Ii', 'II').replace('Iii', 'III').replace('Mcc', 'McC')
            newParty['name'] = normalizedName
            newParty['party'] = record['Party']
            newParty['office'] = record['Office']
            newParty['status'] = record['CommitteeStatus']
            if len(record['District']) > 0:
                newParty['district'] = record['District']
            if len(record['Place']) > 0:
                newParty['place'] = record['Place']
            allParties.append(newParty)
    return numModified

def addDistrictIDs():
    global allParties
    global allDistricts
    numModified = 0
    # Add OCD IDs for state legislators, circuit court judges, county positions, and (lt) governors.
    stateLegPattern = r'^(HOUSE|SENATE) DISTRICT \d+$'
    circuitCourtPattern = r'^\d+(TH|RD|ND|ST) JUDICIAL CIRCUIT$'
    countyPattern = r'^.+ COUNTY$'
    for party in allParties:
        recognized = False # record whether we find a match
        if 'office' in party and (party['office'] == 'GOVERNOR' or party['office'] == 'LT. GOVERNOR'):
            districtID = 'ocd-division/country:us/state:al'
            party['district'] = 'ALABAMA'
            recognized = True
        elif 'district' not in party: # ignore PACs
            continue
        if re.match(stateLegPattern, party['district']) != None:
            districtID = 'ocd-division/country:us/state:al/sld'
            districtID += ('u' if 'SENATE' in party['district'] else 'l')
            districtID += ':' + party['district'].split(' ')[-1]
            recognized = True
        elif re.match(circuitCourtPattern, party['district']) != None:
            districtID = 'ocd-division/country:us/state:al/circuit_court:'
            districtID += party['district'].split(' ')[0][:-2]
            recognized = True
        elif re.match(countyPattern, party['district']) != None:
            districtID = 'ocd-division/country:us/state:al/county:'
            districtID += party['district'][:-7].lower().replace(' ','_').replace('.','')
            recognized = True
        # Add our generated ID into the data if it's valid.
        if recognized:
            # Check if the ocd ID we generated is in the official list.
            valid = sum([d['ocdID'] == districtID for d in allDistricts])
            if not valid:
                print('>> Error: unrecognizable district "' + party['district'] + '"')
            else:
                party['ocdID'] = districtID
                numModified += 1
    return numModified

if __name__=='__main__':
    main()
