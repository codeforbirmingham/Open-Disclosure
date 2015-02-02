#!/usr/bin/python3

########################################################################
#
# File: GenerateTransactionCollection.py
# Last Edit: 2015-02-02
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: This script uses the four data files from alabamavotes.gov
# and the Geocoding file produced by GeocodeData.py to generate a JSON 
# file with every transaction formatted according to the data model.
# The output should have party_id, party_type, party_name, amount, name, 
# filed_date, type, transaction_type, transaction_id, contributor_id,
# and amended for all records.
# -Cash data will also have source_type.
# -Expenditure data will also have explanation and purpose.
# -InKind data will also have inkind_nature and source_type.
# -Receipt data will also have endorsers and source_type.
# Everything is a string except endorsers, which is a list.
#
########################################################################

import json
import csv

GEOCODINGS = '2014_Geocoding.json'
DATAFILES = ['2014_CashContributionsExtract_fixed.csv',
             '2014_ExpendituresExtract_fixed.csv',
             '2014_InKindContributionsExtract.csv',
             '2014_OtherReceiptsExtract.csv']
OUTFILE = '2014_TransactionCollection.json'

def main():
    # Load the geocodings so we can get '_id' values for orgs.
    global allGeocodings
    allGeocodings = []
    with open('../data/' + GEOCODINGS) as datafile:
        allGeocodings = json.load(datafile)
    global allTransactions
    allTransactions = [] # master list of Transactions
    # load the data from each file
    for filename in DATAFILES:
        with open('../data/' + filename, errors='replace', newline='') as datafile:
            scrapeTransactions(csv.reader(datafile))
    # output the data to a file
    print('>> Writing ' + str(len(allTransactions)) + ' records to ' + OUTFILE + '.')
    with open('../data/import/' + OUTFILE, 'w') as datafile:
        json.dump(allTransactions, datafile, sort_keys=True, 
                  indent=4, separators=(',', ': '))

def scrapeTransactions(records):
    # initialize some variables up here so they have a wide enough scope
    record_type = ''
    columnHeaders = []
    # for each record, scrape the data and throw it in allTransactions
    for i, record in enumerate(records):
        if i == 0:
            columnHeaders = record
            record_type = record[1][:-6] # Expenditure, Contribution, or Receipt?
        else:
            thisTransaction = {}
            thisTransaction['type'] = record_type
            thisTransaction['transaction_type'] = record[columnHeaders.index(record_type + 'Type')].strip()
            name = record[3] + ' ' + record[4] + ' ' + record[5] + ' ' + record[6]
            name = name.strip().title() # so organizations don't have trailing spaces and aren't ALL CAPS
            if len(name) > 0: thisTransaction['name'] = name
            # find their record in the geocoding file and get the _id
            try:
                thisTransaction['contributor_id'] = str(allGeocodings[name]['_id'])
            except KeyError:
                thisTransaction['contributor_id'] = '1'
            thisTransaction['party_id'] = record[0]
            partyTypeCol = columnHeaders.index('CommitteeType')
            if record[partyTypeCol] == 'Political Action Committee':
                thisTransaction['party_type'] = 'PAC'
            elif record[partyTypeCol] == 'Principal Campaign Committee':
                thisTransaction['party_type'] = 'Candidate'
            thisTransaction['party_type'] = record[partyTypeCol]
            if len(record[partyTypeCol + 1].strip()) > 0:
                rawName = record[partyTypeCol + 1]
            else:
                rawName = record[partyTypeCol + 2]
            thisTransaction['party_name'] = rawName.title().strip().replace('Pac','PAC').replace('"','').replace('Ii','II').replace('Iii','III')
            thisTransaction['amount'] = record[1]
            thisTransaction['filed_date'] = record[columnHeaders.index('FiledDate')]
            if record_type == 'Expenditure':
                if len(record[11]) > 0: thisTransaction['explanation'] = record[11].lower()
                if len(record[14]) > 0: thisTransaction['purpose'] = record[14].lower()
                thisTransaction['transaction_id'] = record[12]
            else:
                thisTransaction['transaction_id'] = record[11]
                thisTransaction['source_type'] = record[14]
            thisTransaction['amended'] = record[columnHeaders.index('Amended')]
            try: # only works for InKindContributions
                thisTransaction['inkind_nature'] = record[columnHeaders.index('NatureOfInKindContribution')]
            except ValueError:
                pass
            endorsers = []
            if record_type == 'Receipt':
                for index in [19, 22, 25]:
                    endorser = record[index:index+2]
                    if sum(len(field) for field in endorser) > 0:
                        endorsers.append(endorser)
                if len(endorsers) > 0:
                    thisTransaction['endorsers'] = endorsers
            # tack it on to the master list
            allTransactions.append(thisTransaction)

if __name__=='__main__':
    main() 
