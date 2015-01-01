#!/usr/bin/python3

############################################################################
#
# File: GeneratePayeeCollection.py
# Last Edit: 2015-01-01
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: This script uses the Geocoding and ContributorandPayeeLocations
# json files to generate data matching the 'Payee' collection
# in the data model. It uses the ContribPayeeIDs.json file to pick out just
# the payees from the data.
#
############################################################################

import json

CONTRIBPAYEEIDS = '2014_ContribPayeeIDs.json'
GEOCODING = '2014_Geocoding.json'
CONTRIBPAYEELOCATIONS = '2014_ContributorAndPayeeLocations.json'
OUTFILE = '2014_PayeeCollection.json'

def main():
    global allPayees
    allPayees = [] # master list of payees
    global payeeIDs
    payeeIDs = [] # _id values for payees
    # load the payee IDs
    print('>> Loading IDs from ' + CONTRIBPAYEEIDS)
    with open('../data/' + CONTRIBPAYEEIDS) as datafile:
        allIDs = json.load(datafile)
        payeeIDs = allIDs['PayeeIDs'] 
    # start with the output from GeocodeData.py
    print('>> Loading data from ' + GEOCODING + '.')
    with open('../data/' + GEOCODING) as datafile:
       loadPayees(json.load(datafile))
    # add the geographic data from LocateContributorsAndPayees.py
    print('>> Loading data from ' + CONTRIBPAYEELOCATIONS + '.')
    with open('../data/' + CONTRIBPAYEELOCATIONS) as datafile:
        addLocationData(json.load(datafile))    
    # id 1 was assigned to nameless records
    allPayees.append({'_id':1,'name':'NO NAME'})
    # output the data to a file
    print('>> Writing ' + str(len(allPayees)) + ' records to ' + OUTFILE + '.')
    with open('../data/import/' + OUTFILE, 'w') as datafile:
        json.dump(allPayees, datafile, sort_keys=True, 
                  indent=4, separators=(',', ': '))

def loadPayees(geocodings):
    # iterate over each organization and add them to allPayees,
    # formatting according to the data model
    global allPayees
    global payeeIDs
    numOrgs = 0
    for orgName in geocodings:
        oldOrg = geocodings[orgName]
        if oldOrg['_id'] in payeeIDs and len(orgName) > 0:
            numOrgs += 1
            newOrg = {}
            newOrg['name'] = orgName
            newOrg['_id'] = oldOrg['_id']
            newOrg['organization_type'] = oldOrg['orgType']
            newOrg['address'] = oldOrg['addr']
            allPayees.append(newOrg)
    print('>> Loaded ' + str(numOrgs) + ' organizations from ' + GEOCODING + '.')

def addLocationData(locations):
    # Add available location information to allPayees.
    # Jump through hoops to avoid modifying data in an object
    # while iterating over it.
    global allPayees
    newAllPayees = []
    modifiedPayees = 0
    for oldPayee in allPayees:
        newPayee = dict(oldPayee)
        # if location data exists, add it
        for payeeID in locations:
            if str(newPayee['_id']) == payeeID:
                modifiedPayees += 1
                locationData = locations[payeeID]
                newPayee['geo_data'] = locationData['geo_data']
                newPayee['in_state'] = locationData['inState']
                if locationData['inState']:
                    try:
                        newPayee['house_district'] = locationData['house']
                    except KeyError:
                        pass
                    try:
                        newPayee['senate_district'] = locationData['senate']
                    except KeyError:
                        pass
                    try:
                        newPayee['county'] = locationData['county']
                    except KeyError:
                        pass
                break
        newAllPayees.append(newPayee)
    # copy the modified data to the global variable
    allPayees = list(newAllPayees) 
    print('>> Modified ' + str(modifiedPayees) + ' records with location data.')

if __name__=='__main__':
    main() 