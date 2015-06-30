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
    YEAR = config.get('GENERATE_TRANSACTEES', 'YEAR')
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
    # Load the output file from a previous run if it's there so we have the id values.
    global existingTransactees
    existingTransactees = []
    try:
        with open(DATA_DIR + OUTFILE) as datafile:
            existingTransactees = json.load(datafile)
    except FileNotFoundError:
        # This is a fresh run and new id's will be generated.
        pass
    if len(existingTransactees) > 0:
        print('>> Loaded ' + str(len(existingTransactees)) + ' records from ' + OUTFILE)
    # Make a dict out of the existingTransactees so we have constant time access to id values.
    global transacteeIDs
    transacteeIDs = {}
    for entry in existingTransactees:
        if isinstance(entry['transaction_ids'], str): # Undo flattening
            txIDs = json.loads(entry['transaction_ids'].replace('\'', '"'))
        else:
            txIDs = entry['transaction_ids']
        for txID in txIDs:
            transacteeIDs[entry['filed_year'] + entry['transaction_type'] + txID] = entry['id']
    # load data from each source file
    for filename in DATAFILES:
        print('>> Loading data from ' + filename)
        with open(DATA_DIR + filename, 'r', errors='ignore', newline='') as csvfile:
            process(YEAR, csv.DictReader(csvfile), recordTypes[filename])
    # Merge the existing records with the newly found ones (except duplicates)
    numDuplicates = mergeExistingTransactees()
    if len(existingTransactees) > 0:
        print('>> Merged transactees with records from the disk; there were ' + str(numDuplicates) + ' duplicates.')
    print('>> Writing ' + str(len(allTransactees)) + ' records to ' + OUTFILE)
    with open(DATA_DIR + OUTFILE, 'w') as datafile:
        if PRETTY_PRINT:
            json.dump(allTransactees, datafile, sort_keys=True,
                      indent=4, separators=(',', ': '))
        else:
            json.dump(allTransactees, datafile)

# process each record, adding it to allTransactees
# year is the year the data is from, as a string
# records is a csv.DictReader
# recordTypes is (<id col name>, <org type col name>, <transactee type>)
def process(year, records, recordTypes):
    global transacteeIDs
    global allTransactees
    # idCol = ContributionID, ExpenditureID, InKindContributionID, or ReceiptID
    idCol = recordTypes[0]
    # orgTypeCol = ContributorType,  ReceiptSourceType, or ''
    orgTypeCol = recordTypes[1]
    # transacteeType = Contributor, Payee, or ReceiptSource
    transacteeType = recordTypes[2]
    # record the starting index for this type (for efficiency later)
    startIndex = len(allTransactees)
    for record in records:
        name = record['FirstName'] + ' ' + record['MI'] + ' ' + record['LastName'] + ' ' + record['Suffix']
        name = name.strip().title().replace('Ii','II').replace('Iii','III').replace('IIi', 'III').replace('  ', ' ')
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
            # check if they're already in allTransactees (and the same type)
            for record in allTransactees[startIndex:]:
                if record['name'] == name and record['address'] == address:
                    # add this transaction id to the existing record
                    record['transaction_ids'].append(txID)
                    isNew = False
                    break
        if isNew: # we haven't seen them yet
            newOrg = {}
            newOrg['name'] = name
            newOrg['address'] = address
            newOrg['transactee_type'] = transacteeType
            newOrg['transaction_type'] = idCol[:-2]
            # If the transactee id was generated in a previous run, reuse it.
            try:
                newOrg['id'] = transacteeIDs[year + newOrg['transaction_type'] + txID]
            except KeyError:
                newOrg['id'] = str(uuid4()).upper() # random unique id
            newOrg['API_status'] = '' # will be used by geocoding script
            newOrg['organization_type'] = orgType
            newOrg['transaction_ids'] = [txID]
            newOrg['filed_year'] = year
            allTransactees.append(newOrg)

def mergeExistingTransactees():
    global allTransactees
    global existingTransactees
    numDuplicates = 0
    for transactee in existingTransactees:
        if transactee not in allTransactees:
            allTransactees.append(transactee)
        else:
            numDuplicates += 1
    return numDuplicates

if __name__=='__main__':
    main()
