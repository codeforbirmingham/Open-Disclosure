#!/usr/bin/python3

###################################################################
#
# File: GenerateContributorCollection.py
# Last Edit: 2015-03-08
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: This script uses the Geocoding and ContributorLocations
# json files to generate data matching the 'Contributor' collection
# in the data model. It could be made more efficient
# and elegant but it gets the job done.
#
###################################################################

import json

GEOCODING = '2014_Geocoding.json'
CONTRIBPAYEELOCATIONS = '2014_ContributorAndPayeeLocations.json'
OUTFILE = '2014_Contributors.json'

def main():
    global allContributors
    allContributors = [] # master list of Contributors
    # start with the output from GeocodeData.py
    print('>> Loading data from ' + GEOCODING + '.')
    with open('../data/' + GEOCODING) as datafile:
       loadContributors(json.load(datafile))
    # add the geographic data from LocateContributors.py
    print('>> Loading data from ' + CONTRIBPAYEELOCATIONS + '.')
    with open('../data/' + CONTRIBPAYEELOCATIONS) as datafile:
        addLocationData(json.load(datafile))    
    # id 1 was assigned to nameless contributors
    allContributors.append({'_id':1,'name':'NO NAME'})
    # output the data to a file
    print('>> Writing ' + str(len(allContributors)) + ' records to ' + OUTFILE + '.')
    with open('../data/' + OUTFILE, 'w') as datafile:
        json.dump(allContributors, datafile, sort_keys=True, 
                  indent=4, separators=(',', ': '))

def loadContributors(geocodings):
    # iterate over each organization and add them to allContributors,
    # formatting according to the data model
    global allContributors
    global contributorIDs
    numOrgs = 0
    for orgName in geocodings:
        if len(orgName) == 0:
            continue
        oldOrg = geocodings[orgName]
        # check if it's a contributor not a payee
        if 'ContributionIDs' in orgOrg or 'InKindContributionIDs' in orgOrg:
            numOrgs += 1
            newOrg = {}
            newOrg['name'] = orgName
            newOrg['_id'] = oldOrg['_id']
            newOrg['organization_type'] = oldOrg['orgType']
            newOrg['address'] = oldOrg['addr']
            allContributors.append(newOrg)
    print('>> Loaded ' + str(numOrgs) + ' organizations from ' + GEOCODING + '.')

def addLocationData(locations):
    # Add available location information to allContributors.
    # Jump through hoops to avoid modifying data in an object
    # while iterating over it.
    global allContributors
    newAllContributors = []
    modifiedContributors = 0
    for oldContributor in allContributors:
        newContributor = dict(oldContributor)
        # if location data exists, add it
        for contributorID in locations:
            if str(newContributor['_id']) == contributorID:
                modifiedContributors += 1
                locationData = locations[contributorID]
                newContributor['geo_data'] = locationData['geo_data']
                newContributor['in_state'] = locationData['inState']
                if locationData['inState']:
                    try:
                        newContributor['house_district'] = locationData['house']
                    except KeyError:
                        pass
                    try:
                        newContributor['senate_district'] = locationData['senate']
                    except KeyError:
                        pass
                    try:
                        newContributor['county'] = locationData['county']
                    except KeyError:
                        pass
                break
        newAllContributors.append(newContributor)
    # copy the modified data to the global variable
    allContributors = list(newAllContributors) 
    print('>> Modified ' + str(modifiedContributors) + ' records with location data.')

if __name__=='__main__':
    main() 
