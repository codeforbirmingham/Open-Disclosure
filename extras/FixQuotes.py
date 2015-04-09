#!/usr/bin/python3

# Fix Quotes in the csv's with party information

import csv

def main():
    c = csv.reader(open('/home/matthew/Desktop/Open-Disclosure/data/2014_Parties_active.csv'))
    newC = []
    for record in c:
        newRecord = []
        for field in record:
            newField = field.replace('"', '')
            newField = newField.strip()
            newRecord.append(newField)
        newC.append(newRecord)
    with open('/home/matthew/Desktop/Open-Disclosure/data/2014_Parties_active_fixed.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(newC)

main()
