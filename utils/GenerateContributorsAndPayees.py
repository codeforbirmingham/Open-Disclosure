#!/usr/bin/python3

##############################################################################
#
# File: GenerateContributorsAndPayees.py
# Last Edit: 2015-03-16
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: This script reads the four data files from 
# http://fcpa.alabamavotes.gov/PublicSite/DataDownload.aspx
# and outputs lists of contributors and payees that can later
# be geocoded. Sources of receipts are considered contributors.
# The txIDs are the unique identifiers for rows in the data files,
# so either ReceiptID, ExpenditureID, InKindContributionID, or ContributionID
# depending on the file. They are only unique within their own file. 
# The data format is documented on the GitHub wiki.
#
##############################################################################

import sys
import json
import csv
from uuid import uuid4

DATAFILES = ['2014_CashContributionsExtract_fixed.csv',
             '2014_ExpendituresExtract_fixed.csv',
             '2014_InKindContributionsExtract.csv',
             '2014_OtherReceiptsExtract.csv']
HEADERS = ['_id', '_API_status', 'name', 'organization_type', 'address']
CONTRIBS_OUTFILE = '2014_Contributors' # file extension will be added
PAYEES_OUTFILE = '2014_Payees' # file extension will be added
OUTPUT_JSON = True # otherwise output CSV
CONTRIBS_OUTFILENAME = CONTRIBS_OUTFILE + ('.json' if OUTPUT_JSON else '.csv')
PAYEES_OUTFILENAME = PAYEES_OUTFILE + ('.json' if OUTPUT_JSON else '.csv')
PRETTY_PRINT = True # controls JSON output formatting

def main():
    global allContributors
    allContributors = [] # master list of Contributors
    global allPayees
    allPayees = [] # master list of Payees
    # hard code the ID and org type column names for each file type
    colNames = {}
    for filename in DATAFILES:
        if 'CashContribution' in filename:
            colNames[filename] = ('ContributionID', 'ContributorType')
        elif 'Expenditure' in filename:
            colNames[filename] = ('ExpenditureID', '')
        elif 'InKindContribution' in filename:
            colNames[filename] = ('InKindContributionID', 'ContributorType')
        elif 'OtherReceipts' in filename:
            colNames[filename] = ('ReceiptID', 'ReceiptSourceType')
        else:
            print('>> Unrecognized filename: ' + filename + '. Quitting.')
            sys.exit(1)
    # load data from each source file
    for filename in DATAFILES:
        print('>> Loading data from ' + filename + '.')
        with open('../data/' + filename, 'r', errors='ignore', newline='') as csvfile:
            process(csv.DictReader(csvfile), colNames[filename])
    # output the data to two files
    print('>> Writing ' + str(len(allContributors)) + ' records to ' + CONTRIBS_OUTFILENAME + '.')
    if OUTPUT_JSON:
        with open('../data/' + CONTRIBS_OUTFILENAME, 'w') as datafile:
            if PRETTY_PRINT:
                json.dump(allContributors, datafile, sort_keys=True, 
                          indent=4, separators=(',', ': '))
            else:
                json.dump(allContributors, datafile)
    else: # output CSV
        with open('../data/' + CONTRIBS_OUTFILENAME, 'w', newline='') as datafile:
            writer = csv.DictWriter(datafile, quoting=csv.QUOTE_ALL, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(allContributors)
    print('>> Writing ' + str(len(allPayees)) + ' records to ' + PAYEES_OUTFILENAME + '.')
    if OUTPUT_JSON:
        with open('../data/' + PAYEES_OUTFILENAME, 'w') as datafile:
            if PRETTY_PRINT:
                json.dump(allPayees, datafile, sort_keys=True, 
                          indent=4, separators=(',', ': '))
            else:
                json.dump(allPayees, datafile)
    else: # output CSV
        with open('../data/' + PAYEES_OUTFILENAME, 'w', newline='') as datafile:
            writer = csv.DictWriter(datafile, quoting=csv.QUOTE_ALL, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(allPayees)

# process each record, adding to allContributors or allPayees
# records is a csv.DictReader and colNames is (<id col name>, <org type col name>)
def process(records, colNames):
    global allContributors
    global allPayees
    idCol = colNames[0] # ContributionID for example
    idType = colNames[0] + 's' # ExpenditureIDs for example
    orgTypeCol = colNames[1] # ContributorType for example
    for record in records:
        name = record['FirstName'] + ' ' + record['MI'] + ' ' + record['LastName'] + ' ' + record['Suffix']
        name = name.strip().title().replace('Ii','II').replace('Iii','III') 
        address = record['Address1'] + ' ' + record['City'] + ' ' + record['State'] + ' ' + record['Zip']
        address = address.strip()
        txID = record[idCol]
        isContributor = True
        try:
            orgType = record[orgTypeCol]
        except KeyError: # must be expenditure data
            orgType = ''
            isContributor = False
        isNew = True
        # check if they're already in allContributors or allPayees
        for record in (allContributors if isContributor else allPayees):
            if record['name'] == name and record['address'] == address:
                # if it's the same type of contributor, update it with this txID
                try:
                    record[idType].append(txID)
                # otherwise keep looking
                except KeyError:
                    continue
                record[idType] = list(set(record[idType])) # remove any dupes
                isNew = False
                break
        # otherwise we haven't seen this yet
        if isNew:
            newOrg = {}
            newOrg['name'] = name
            newOrg['_id'] = str(uuid4()).upper() # random unique id
            newOrg['_API_status'] = '' # will be used by geocoding script
            newOrg['organization_type'] = orgType
            newOrg[idType] = [txID]
            newOrg['address'] = address 
            if isContributor:
                allContributors.append(newOrg)
            else:
                allPayees.append(newOrg)

if __name__=='__main__':
    main() 
