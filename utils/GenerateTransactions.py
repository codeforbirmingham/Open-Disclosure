#!/usr/bin/python3

########################################################################
#
# File: GenerateTransactions.py
# Last Edit: 2015-03-27
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script uses the four data files from alabamavotes.gov
# and the file produced by GenerateTransactees.py (for IDs)
# to collect every transaction formatted according to the data model.
# The output should have party_id, amount, filed_date, type,
# transaction_type, transaction_id, transactee_id, and
# amended for all records.
# -Expenditure data will also have explanation and purpose.
# -InKind data will also have inkind_nature and source_type.
# -Receipt data will also have endorsers and source_type.
# Everything is a string except endorsers, which is a list.
# Output can be in either JSON or CSV format.
#
########################################################################

import json
import csv

TRANSACTEES_FILE = '2014_Transactees.json'
DATAFILES = ['2014_CashContributionsExtract_fixed.csv',
             '2014_ExpendituresExtract_fixed.csv',
             '2014_InKindContributionsExtract.csv',
             '2014_OtherReceiptsExtract.csv']
OUTFILE = '2014_Transactions' # file extension will be added
OUTPUT_JSON = True # otherwise output CSV
PRETTY_PRINT = True # controls JSON output format
OUTFILENAME = OUTFILE + ('.json' if OUTPUT_JSON else '.csv')
HEADERS = ['type', 'transaction_type', 'name', 'transactee_id', 'party_id', 'amount', 'filed_date', 'explanation', 'purpose', 'transaction_id', 'source_type', 'amended', 'inkind_nature', 'endorsers']

def main():
    global allTransactees
    allTransactees = []
    # First load the Transactees
    with open('../data/' + TRANSACTEES_FILE) as datafile:
        allTransactees = json.load(datafile)
    print('>> Loaded ' + str(len(allTransactees)) + ' records from ' + TRANSACTEES_FILE + '.')
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
    global allTransactees
    # idCol = ContributionID, ExpenditureID, InKindContributionID, or ReceiptID
    idCol = recordType + 'ID'
    # recordType = Contribution, Expenditure, or Receipt
    if recordType == 'InKindContribution':
        recordType = recordType[6:]
    # for each record, scrape the data and throw it in allTransactions
    for record in records:
        thisTransaction = {}
        thisTransaction['type'] = idCol[:-2] # cut off 'ID' part
        thisTransaction['transaction_type'] = record[recordType + 'Type'].strip()
        # find their record in allTransactees and get the _id
        foundMatch = False
        for entry in allTransactees:
            # if the txID's match, copy the UUID.
            if idCol + 's' in entry and record[idCol] in entry[idCol + 's']:
                thisTransaction['transactee_id'] = entry['_id']
                foundMatch = True
                break
        if not foundMatch:
            print('Error: No match found for ' + name + ' ' + address + ' in the transactees file.')
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
