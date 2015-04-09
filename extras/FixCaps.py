#!/usr/bin/python3

# reads in "2014_Parties_active_fixed.csv" and "2014_Parties_dissolved.csv"
# and calls .title() on each field to fix the ALL CAPS data.

import csv

def main():
    f = open('../data/2014_Parties_active_fixed.csv')
    f2 = open('../data/2014_Parties_dissolved.csv')
    fo = open('../data/2014_Parties_active_fixed2.csv', 'w')
    f2o = open('../data/2014_Parties_dissolved_fixed.csv', 'w')
    records = csv.reader(f)
    newRecords = []
    records2 = csv.reader(f2)
    newRecords2 = []
    for i, record in enumerate(records):
        newRecord = []
        for field in record:
            newRecord.append(field.title())
        newRecords.append(newRecord)
    for record in records2:
        newRecord = []
        for j, field in enumerate(record):
            newRecord.append(field.title())
        newRecords2.append(newRecord)
    writer = csv.writer(fo, quoting=csv.QUOTE_ALL)
    writer.writerows(newRecords)
    writer2 = csv.writer(f2o, quoting=csv.QUOTE_ALL)
    writer2.writerows(newRecords2)

main()
