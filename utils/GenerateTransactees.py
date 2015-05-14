#!/usr/bin/python3

##############################################################################
#
# File: GenerateTransactees.py
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script reads the four data files from
# http://fcpa.alabamavotes.gov/PublicSite/DataDownload.aspx
# and makes a list of transactees (contributors, payees, and receipt sources)
# that can be geocoded. Transactees refer to people or organizations who do
# business with (or contribute to) political parties (PACs/Candidates).
# The txIDs are the unique identifiers for rows in the data files,
# so either ReceiptID, ExpenditureID, InKindContributionID, or ContributionID
# depending on the file. They are only unique within their own file.
# The data format is documented on the GitHub wiki. Configuration parameters
# will be read from 'config.ini' in the current directory.
#
##############################################################################

import sys
import json
import csv
from uuid import uuid4
from datetime import datetime
from configparser import ConfigParser

def main():
    # Read the config file.
    config = ConfigParser()
    config.read('config.ini')
    DATA_DIR = config.get('GENERATE_TRANSACTEES', 'DATA_DIR')
    DATAFILES = json.loads(config.get('GENERATE_TRANSACTEES', 'DATAFILES'))
    OUTFILE = config.get('GENERATE_TRANSACTEES', 'OUTFILE')
    PRETTY_PRINT = config.getboolean('GENERATE_TRANSACTEES', 'PRETTY_PRINT')
    global allTransactees
    allTransactees = [] # master list of Transactees
    # hard code the ID column, org type column, and transactee type for each file
    recordTypes = {}
    for filename in DATAFILES:
        if 'CashContribution' in filename:
            recordTypes[filename] = ('ContributionID', 'ContributorType', 'Contributor')
        elif 'Expenditure' in filename:
            recordTypes[filename] = ('ExpenditureID', '', 'Payee')
        elif 'InKindContribution' in filename:
            recordTypes[filename] = ('InKindContributionID', 'ContributorType', 'Contributor')
        elif 'OtherReceipts' in filename:
            recordTypes[filename] = ('ReceiptID', 'ReceiptSourceType', 'ReceiptSource')
        else:
            print('>> Unrecognized filename: ' + filename + '. Quitting.')
            sys.exit(1)
    # load data from each source file
    for filename in DATAFILES:
        print('>> Loading data from ' + filename)
        with open(DATA_DIR + filename, 'r', errors='ignore', newline='') as csvfile:
            process(csv.DictReader(csvfile), recordTypes[filename])
    print('>> Writing ' + str(len(allTransactees)) + ' records to ' + OUTFILE)
    with open(DATA_DIR + OUTFILE, 'w') as datafile:
        if PRETTY_PRINT:
            json.dump(allTransactees, datafile, sort_keys=True,
                      indent=4, separators=(',', ': '))
        else:
            json.dump(allTransactees, datafile)

# process each record, adding it to allTransactees
# records is a csv.DictReader and recordTypes is (<id col name>, <org type col name>, <transactee type>)
def process(records, recordTypes):
    global allTransactees
    # idCol = ContributionID, ExpenditureID, InKindContributionID, or ReceiptID
    idCol = recordTypes[0]
    idType = idCol + 's'
    # orgTypeCol = ContributorType,  ReceiptSourceType, or ''
    orgTypeCol = recordTypes[1]
    # transacteeType = Contributor, Payee, or ReceiptSource
    transacteeType = recordTypes[2]
    # record the starting index for this type (for efficiency later)
    startIndex = len(allTransactees)
    for record in records:
        name = record['FirstName'] + ' ' + record['MI'] + ' ' + record['LastName'] + ' ' + record['Suffix']
        name = name.strip().title().replace('Ii','II').replace('Iii','III').replace('  ', ' ')
        if name[-3:].upper() == 'PAC':
            name = name[:-3] + 'PAC'
        address = record['Address1'] + ' ' + record['City'] + ' ' + record['State'] + ' ' + record['Zip']
        address = address.strip().replace('  ',' ')
        txID = record[idCol]
        try:
            orgType = record[orgTypeCol]
        except KeyError: # must be Expenditure data
            orgType = ''
        isNew = True
        # treat each nameless person as unique
        if len(name) != 0:
            # check if they're already in allTransactees
            for record in allTransactees[startIndex:]:
                if record['name'] == name and record['address'] == address and record['transactee_type'] == transacteeType:
                    # add this transaction id to the existing record
                    if idType not in record['transaction_ids']:
                        record['transaction_ids'][idType] = [txID]
                    else:
                        record['transaction_ids'][idType].append(txID)
                    isNew = False
                    break
        if isNew: # we haven't seen them yet
            newOrg = {}
            newOrg['name'] = name
            newOrg['transactee_type'] = transacteeType
            newOrg['id'] = str(uuid4()).upper() # random unique id
            newOrg['API_status'] = '' # will be used by geocoding script
            newOrg['organization_type'] = orgType
            newOrg['transaction_ids'] = {idType : [txID]}
            newOrg['address'] = address
            allTransactees.append(newOrg)

if __name__=='__main__':
    main()
