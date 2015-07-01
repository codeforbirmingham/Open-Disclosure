#!/usr/bin/python3

###############################################################################
#
# File: CompareYears.py
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: Examine Transactee and Party data that may span multiple years.
# If both the name and address of a contributor match, change the more recent 
# dataset(s) to make the unique id's match. If the name, office, and district 
# of a candidate match, or if their openstates_id or influenceexplorer_id 
# values match, make the unique id values match. For a PAC, a matching name 
# is sufficient to assume equality. This means we can identify 
# PACs/Candidates/Contributors/etc. across years. The modified transactee and 
# party data is written back out to the disk.
#
###############################################################################

import sys
import json
from configparser import ConfigParser

def main():
    config = ConfigParser()
    config.read('config.ini')
    DATA_DIR = config.get('COMPARE_YEARS', 'DATA_DIR')
    TRANSACTEES_FILE = config.get('GENERATE_TRANSACTEES', 'OUTFILE')
    PARTIES_FILE = config.get('GENERATE_PARTIES', 'OUTFILE')
    PRETTY_PRINT = config.get('COMPARE_YEARS', 'PRETTY_PRINT')
    global allTransactees
    allTransactees = []
    try:
        with open(DATA_DIR + TRANSACTEES_FILE) as f:
            allTransactees = json.load(f)
    except FileNotFoundError:
        print('>> Error: ' + TRANSACTEES_FILE + ' not found!')
        sys.exit(2)
    if len(allTransactees) == 0:
        print('>> Error: no transactees found in ' + TRANSACTEES_FILE)
        sys.exit(2)
    else:
        print('>> Loaded ' + str(len(allTransactees)) + ' records from ' + TRANSACTEES_FILE)
    global allParties
    allParties = []
    try:
        with open(DATA_DIR + PARTIES_FILE) as f:
            allParties = json.load(f)
    except FileNotFoundError:
        print('>> Error: ' + PARTIES_FILE + ' not found!')
        sys.exit(2)
    if len(allParties) == 0:
        print('>> Error: no parties found in ' + PARTIES_FILE)
        sys.exit(2)
    else:
        print('>> Loaded ' + str(len(allParties)) + ' records from ' + PARTIES_FILE)
    # All the data should be loaded; now analyze it.
    # To improve efficiency, sort data by filed_year, and record how many are from each year
    (transacteesSetLengths, partiesSetLengths) = sortByYear()
    # Define which fields must match for each entity type to be considered equal.
    fieldComparisons = {'Transactee': ['name', 'address'],
                        'Candidate': ['name', 'office', 'district'],
                        'PAC': ['name']}
    # modify id's in allTransactees
    transacteesModified = compareYears(True, transacteesSetLengths, fieldComparisons)
    # modify id's in allParties
    partiesModified = compareYears(False, partiesSetLengths, fieldComparisons)
    print('>> Modified ' + str(transacteesModified) + ' transactee records and ' + str(partiesModified) + ' party records.')
    # Write the transactee and party data to the disk.
    print('>> Writing ' + str(len(allTransactees)) + ' records to ' + TRANSACTEES_FILE)
    with open(DATA_DIR + TRANSACTEES_FILE, 'w') as f:
        if PRETTY_PRINT:
           json.dump(allTransactees, f, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            json.dump(allTransactees, f)
    print('>> Writing ' + str(len(allParties)) + ' records to ' + PARTIES_FILE)
    with open(DATA_DIR + PARTIES_FILE, 'w') as f:
        if PRETTY_PRINT:
           json.dump(allParties, f, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            json.dump(allParties, f)

def countRecordsByYear(records):
    setLengths = {}
    for record in records:
        if record['filed_year'] in setLengths:
            setLengths[record['filed_year']] += 1
        else:
            setLengths[record['filed_year']] = 1
    return setLengths

def arrangeByYear(records):
    byYear = {}
    for record in records:
        if record['filed_year'] in byYear:
            byYear[record['filed_year']].append(record)
        else:
            byYear[record['filed_year']] = [record]
    years = list(byYear.keys())
    years.sort()
    combined = []
    setLengths = {}
    for year in years:
        setLengths[year] = len(byYear[year])
        combined += byYear[year]
    return (combined, setLengths)
    
def sortByYear():
    '''
    Sort allTransactees and allParties by filed_year.
    :returns: a tuple with mappings from years to number of records for transactees and parties
    '''
    global allTransactees
    global allParties
    # First count how many records exist for each filing year
    transacteeSetLengths = countRecordsByYear(allTransactees)
    partiesSetLengths = countRecordsByYear(allParties)
    # Now sort records by year in linear time
    (sortedAllTransactees, transacteesSetLengths) = arrangeByYear(allTransactees)
    (sortedAllParties, partiesSetLengths) = arrangeByYear(allParties)
    # copy the data into the global variables
    allTransactees = sortedAllTransactees.copy()
    allParties = sortedAllParties.copy()
    # return the number of records in each year for each data type
    return (transacteesSetLengths, partiesSetLengths)

def compareYears(transacteesOrParties, setLengths, fieldComparisons):
    years = list(setLengths.keys())
    years.sort()
    numModified = 0
    lastIndex = -1 # end of previous year's dataset
    dataset = (allTransactees if transacteesOrParties else allParties)
    for year in years[:-1]:
        yearStart = lastIndex + 1
        yearEnd = yearStart + setLengths[year] - 1
        for i in range(yearStart, yearEnd + 1):
            originalRecord = dataset[i]
            if 'transactee_type' in originalRecord: originalRecordType = 'Transactee'
            if 'type' in originalRecord: originalRecordType = originalRecord['type']
            for j in range(yearEnd + 1, len(dataset)):
                record = dataset[j]
                if 'transactee_type' in record: recordType = 'Transactee'
                if 'type' in record: recordType = record['type']
                if recordType != originalRecordType: continue
                '''
                print('recordType='+recordType)
                print('originalRecord='+str(originalRecord))
                print('record='+str(record))
                print('fieldComparisons='+str(fieldComparisons[recordType]))
                '''
                compare = [record[field] == originalRecord[field] for field in fieldComparisons[recordType]]
                #print(compare)
                same = all(compare)
                if same:
                    #TODO should we merge them into one instead of copying the ID?
                    record['id'] = originalRecord['id']
                    numModified += 1
        lastIndex = yearEnd
    return numModified


if __name__=='__main__':
    main()
