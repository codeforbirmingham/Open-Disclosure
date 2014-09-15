#!/usr/bin/python3

##################################################################
#
# File: FindUniqueOrganizations.py
# Last Edit: 9.14.14
# Author: Matthew Leeds
# Purpose: This script reads the four CSV files from
# http://fcpa.alabamavotes.gov/PublicSite/DataDownload.aspx
# and finds each unique organization that's recieving donations,
# which are political candidates and political action committees,
# and exports that data to "YEAR_Organizations.json". If the data
# is formatted similarly next year, you should only have to change
# the DATAFILES and OUTFILE constants.
#
##################################################################

import csv
import json

DATAFILES = ['2014_CashContributionsExtract_fixed.csv',
             '2014_ExpendituresExtract_fixed.csv',
             '2014_InKindContributionsExtract.csv',
             '2014_OtherReceiptsExtract.csv']
OUTFILE = '2014_Organizations.json'

def main():
    global listOfOrgIDs
    listOfOrgIDs = [] # list of OrgID's already recorded
    global listOfOrgs
    listOfOrgs = [] # list of organizations' ID, name, and type
    for filename in DATAFILES:
        # for each file, look for unique organizations
        with open('../data/' + filename, 'r', errors='replace', newline='') as csvfile:
            getOrgs(csv.reader(csvfile))
    # export the data in json format
    with open('../data/' + OUTFILE, 'w') as output:
        json.dump(listOfOrgs, output) 

def getOrgs(records):
    # iterate over the records looking for new information
    for i, record in enumerate(records):
        if i == 0:
            OrgIDColumn = record.index('OrgID')
            CommitteeTypeColumn = record.index('CommitteeType')
            CommitteeNameColumn = record.index('CommitteeName')
            CandidateNameColumn = record.index('CandidateName')
        else:
            # if it's a new OrgID, gather the info
            if record[OrgIDColumn] not in listOfOrgIDs:
                listOfOrgIDs.append(record[OrgIDColumn])
                thisOrg = {} 
                thisOrg['id'] = record[OrgIDColumn]
                thisOrg['type'] = record[CommitteeTypeColumn]
                if len(record[CommitteeNameColumn]) > 1:
                    thisOrg['name'] = record[CommitteeNameColumn]
                else:
                    thisOrg['name'] = record[CandidateNameColumn]
                listOfOrgs.append(thisOrg)

if __name__=='__main__':
    main()
