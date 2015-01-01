#!/usr/bin/python3

######################################################################
#
# File: SeparateContribPayee.py
# Last Edit: 2015-01-01
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: Unfortunately I forgot to distinguish between
# contributors and payees when I wrote LocateContributorsAndPayees.py
# We need to determine which IDs belong to which group. This is 
# accomplished by reading 2014_Geocoding.json and finding _id numbers
# for ones with ContributionIDs or InKindContributionIDs and finding
# ones with ExpenditureIDs or ReceiptIDs, and outputting both lists
# in the format:
# {'ContributorIDs': [640,30656,...], 'PayeeIDs': [1380,3549,...]}
# Note that these groups are not mutually exclusive.
#
######################################################################

import json

def main():
    with open('../data/2014_Geocoding.json') as f:
        j = json.load(f)
    allContributorIDs = []
    allPayeeIDs = []
    for entityName in j:
        entityInfo = j[entityName]
        if 'ContributionIDs' in entityInfo or 'InKindContributionIDs' in entityInfo:
            allContributorIDs.append(entityInfo['_id'])
        if 'ExpenditureIDs' in entityInfo or 'ReceiptIDs' in entityInfo:
            allPayeeIDs.append(entityInfo['_id'])
    outDict = {'ContributorIDs': allContributorIDs, 'PayeeIDs': allPayeeIDs}
    with open('../data/2014_ContribPayeeIDs.json', 'w') as outfile:
        json.dump(outDict, outfile)

if __name__=='__main__':
    main()
