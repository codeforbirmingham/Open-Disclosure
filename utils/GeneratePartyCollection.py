#!/usr/bin/python3

###################################################################
#
# File: GeneratePartyCollection.py
# Last Edit: 2014-12-18
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: This script uses the Organizations and Parties
# data files to generate data matching the 'Party' collection in
# the data model.
#
###################################################################

import csv
import json

UNIQUEORGS = '2014_Organizations.json'
PARTYINFO = ['2014_Parties_active_fixed.csv', '2014_Parties_dissolved.csv']
OUTFILE = '2014_PartyCollection.json'

def main():
    global allParties
    allParties = [] # master list of Party information
    # start with the output from FindUniqueOrganizations.py
    with open('../data/' + UNIQUEORGS) as datafile:
       allParties = json.load(datafile) 
    # add the info we have on each candidate
    for filename in PARTYINFO:
        with open('../data/' + filename) as datafile:
            getCandidateInfo(csv.reader(datafile))    
    # output the data to a file
    with open('../data/import/' + OUTFILE, 'w') as datafile:
        json.dump(allParties, datafile, sort_keys=True, 
                  indent=4, separators=(',', ': '))

def getCandidateInfo(records):
    # iterate over the records and add the info to allParties
    for i, record in enumerate(records):
        if i == 0:
            CandidateNameCol = record.index('CandidateName')
            PartyCol = record.index('Party')
            OfficeCol = record.index('Office')
            DistrictCol = record.index('District')
            PlaceCol = record.index('Place')
            CommitteeStatusCol = record.index('CommitteeStatus')
            CommitteeIDCol = record.index('CommitteeID')
        else:
            # if the ID is in the data, add to it
            for party in allParties:
                if party['_id'] == record[CommitteeIDCol]:
                    party['name'] = record[CandidateNameCol]
                    party['party'] = record[PartyCol]
                    party['office'] = record[OfficeCol]
                    if len(record[DistrictCol]) > 0: 
                        party['district'] = record[DistrictCol]
                    if len(record[PlaceCol]) > 0:
                        party['place'] = record[PlaceCol]
                    party['status'] = record[CommitteeStatusCol]
                    break # don't waste time looking for another match

if __name__=='__main__':
    main() 
