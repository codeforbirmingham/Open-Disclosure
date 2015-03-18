#!/usr/bin/python3

########################################################################
#
# File: GenerateTransactions.py
# Last Edit: 2015-03-17
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script uses the four data files from alabamavotes.gov
# and the files produced by GenerateContributorsAndPayees.py (for IDs)
# to collect every transaction formatted according to the data model.
# The output should have party_id, amount, filed_date, type,
# transaction_type, transaction_id, contributor_id or payee_id, and
# amended for all records.
# -Expenditure data will also have explanation and purpose.
# -InKind data will also have inkind_nature and source_type.
# -Receipt data will also have endorsers and source_type.
# Everything is a string except endorsers, which is a list.
# Output can be in either JSON or CSV format.
#
# This script requires Python 3.4 or later.
#
########################################################################

import json
import csv
from contextlib import suppress

CONTRIBS_FILE = '2014_Contributors.json'
PAYEES_FILE = '2014_Payees.json'
DATAFILES = ['2014_CashContributionsExtract_fixed.csv',
             '2014_ExpendituresExtract_fixed.csv',
             '2014_InKindContributionsExtract.csv',
             '2014_OtherReceiptsExtract.csv']
OUTFILE = '2014_Transactions' # file extension will be added
OUTPUT_JSON = True # otherwise output CSV
PRETTY_PRINT = True # controls JSON output format
OUTFILENAME = OUTFILE + ('.json' if OUTPUT_JSON else '.csv')
HEADERS = ['type', 'transaction_type', 'name', 'contributor_id', 'payee_id', 'party_id', 'amount', 'filed_date', 'explanation', 'purpose', 'transaction_id', 'source_type', 'amended', 'inkind_nature', 'endorsers']

def main():
    global allContributors
    allContributors = []
    global allPayees
    allPayees = []
    # First load the Contributors and Payees
    with open('../data/' + CONTRIBS_FILE) as datafile:
        allContributors = json.load(datafile)
    print('>> Loaded ' + str(len(allContributors)) + ' records from ' + CONTRIBS_FILE + '.')
    with open('../data/' + PAYEES_FILE) as datafile:
        allPayees = json.load(datafile)
    print('>> Loaded ' + str(len(allPayees)) + ' records from ' + PAYEES_FILE + '.')
    # hard code the values of record types for each file
    recordTypes = {}
    for filename in DATAFILES:
        if 'CashContribution' in filename:
            recordTypes[filename] = 'Contribution'
        elif 'InKindContribution' in filename:
            recordTypes[filename] = 'InKindContribution'
        elif 'Expenditure' in filename:
            recordTypes[filename] = 'Expenditure'
        elif 'OtherReceipts' in filename:
            recordTypes[filename] = 'Receipt'
        else:
            print('>> Unrecognized filename: ' + filename + '. Quitting.')
            sys.exit(1)
    global allTransactions
    allTransactions = [] # master list of Transactions
    # Now load the transaction data from each file
    for filename in DATAFILES:
        with open('../data/' + filename, errors='ignore', newline='') as datafile:
            scrapeTransactions(csv.DictReader(datafile), recordTypes[filename])
    # output the data to a file
    print('>> Writing ' + str(len(allTransactions)) + ' records to ' + OUTFILENAME + '.')
    if OUTPUT_JSON:
        with open('../data/' + OUTFILENAME, 'w') as datafile:
            if PRETTY_PRINT:
                json.dump(allTransactions, datafile, sort_keys=True,
                          indent=4, separators=(',', ': '))
            else:
                json.dump(allTransactions, datafile)
    else: # output CSV
        with open('../data/' + OUTFILENAME, 'w', newline='') as datafile:
            writer = csv.DictWriter(datafile, quoting=csv.QUOTE_ALL, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(allTransactions)

def scrapeTransactions(records, recordType):
    global allTransactions
    global allContributors
    global allPayees
    # idCol = ContributionID, ExpenditureID, InKindContributionID, or ReceiptID
    idCol = recordType + 'ID'
    # recordType = Contribution, Expenditure, or Receipt
    if recordType == 'InKindContribution':
        recordType = recordType[6:]
    # for each record, scrape the data and throw it in allTransactions
    for record in records:
        thisTransaction = {}
        thisTransaction['type'] = recordType
        thisTransaction['transaction_type'] = record[recordType + 'Type'].strip()
        # the method of cleaning up the name and address must be the same as in GenerateContributorsAndPayees.py
        name = record['FirstName'] + ' ' + record['MI'] + ' ' + record['LastName'] + ' ' + record['Suffix']
        name = name.strip().title().replace('Ii','II').replace('Iii','III').replace('  ',' ')
        address = record['Address1'] + ' ' + record['City'] + ' ' + record['State'] + ' ' + record['Zip']
        address = address.strip().replace('  ',' ')
        # find their record in allContributors or allPayees and get the _id
        idType = ('payee_id' if recordType == 'Expenditure' else 'contributor_id')
        foundMatch = False
        for entry in (allPayees if recordType == 'Expenditure' else allContributors):
            if entry['name'] == name and entry['address'] == address:
                thisTransaction[idType] = entry['_id']
                foundMatch = True
                break
        if not foundMatch:
            print('Error: No match found for ' + name + ' ' + address + ' in the contributors or payees files.')
        # add some general information
        thisTransaction['party_id'] = record['OrgID']
        thisTransaction['amount'] = record[recordType + 'Amount']
        thisTransaction['filed_date'] = record['FiledDate']
        thisTransaction['transaction_id'] = record[idCol]
        thisTransaction['amended'] = record['Amended']
        # add information specific to this record type
        if recordType == 'Expenditure':
            thisTransaction['explanation'] = record['Explanation'].lower()
            thisTransaction['purpose'] = record['Purpose'].lower()
        elif recordType == 'Receipt':
            endorsers = []
            colNames = ['EndorserName', 'EndorserAddress', 'EndorserGuaranteedAMT']
            with suppress(KeyError):
                for val in ['1','2','3']:
                    endorser = [record[colNames[0] + val], record[colNames[1] + val], record[colNames[2] + val]]
                    if sum(len(field) for field in endorser) > 0:
                        endorsers.append(endorser)
            if len(endorsers) > 0:
                thisTransaction['endorsers'] = endorsers
        elif idCol.startswith('InKindContribution'):
            thisTransaction['inkind_nature'] = record['NatureOfInKindContribution']
        allTransactions.append(thisTransaction)

if __name__=='__main__':
    main()
