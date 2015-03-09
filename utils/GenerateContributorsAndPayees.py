#!/usr/bin/python3

###################################################################
#
# File: GenerateContributorsAndPayees.py
# Last Edit: 2015-03-08
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: This script uses the Geocoding file and some Alabama
# geographic data to locate contributors and payees (by county,
# district, etc) and output the data to two files.
#
###################################################################

import json
import sys
from shapely.geometry import Point, shape

GEOCODING = '2014_Geocoding.json'
STATE_FILE = 'AL.geojson'
COUNTIES_FILE = 'AL_Counties.geojson'
UPPER_DISTRICTS = 'sldu-simple.json'
LOWER_DISTRICTS = 'sldl-simple.json'
CONTRIBS_OUTFILE = '2014_Contributors.json'
PAYEES_OUTFILE = '2014_Payees.json'
PRETTY_PRINT = True # controls JSON output formatting

def main():
    global allContributors
    allContributors = [] # master list of Contributors
    global allPayees
    allPayees = [] # master list of Payees
    # start with the output from GeocodeData.py
    print('>> Loading data from ' + GEOCODING + '.')
    try:
        with open('../data/' + GEOCODING) as datafile:
            loadEntities(json.load(datafile))
    except FileNotFoundError:
        print('>> Error opening ' + GEOCODING + '. Try running GeocodeData.py first.')
        sys.exit(1)
    # locate contributors and payees by county, district, etc.
    locateContributorsAndPayees()
    # id 1 was assigned to nameless contributors
    allContributors.append({'_id':1,'name':'NO NAME'})
    # output the data to two files
    print('>> Writing ' + str(len(allContributors)) + ' records to ' + CONTRIBS_OUTFILE + '.')
    with open('../data/' + CONTRIBS_OUTFILE, 'w') as datafile:
        if PRETTY_PRINT:
            json.dump(allContributors, datafile, sort_keys=True, 
                      indent=4, separators=(',', ': '))
        else:
            json.dump(allContributors, datafile)
    print('>> Writing ' + str(len(allPayees)) + ' records to ' + PAYEES_OUTFILE + '.')
    with open('../data/' + PAYEES_OUTFILE, 'w') as datafile:
        if PRETTY_PRINT:
            json.dump(allPayees, datafile, sort_keys=True, 
                      indent=4, separators=(',', ': '))
        else:
            json.dump(allPayees, datafile)

def loadEntities(geocodings):
    # iterate over each organization and add them to allContributors or allPayees
    global allContributors
    global allPayees
    numOrgs = 0
    for orgName in geocodings:
        if len(orgName) == 0:
            continue
        oldOrg = geocodings[orgName]
        newOrg = {}
        newOrg['name'] = orgName
        newOrg['_id'] = oldOrg['_id']
        newOrg['organization_type'] = oldOrg['orgType']
        newOrg['address'] = oldOrg['addr']
        if len(oldOrg['coords']) > 0:
            newOrg['geo_data'] = [round(oldOrg['coords']['lng'], 6), round(oldOrg['coords']['lat'], 6)]
        # check if it's a contributor or a payee
        if 'ContributionIDs' in oldOrg or 'InKindContributionIDs' in oldOrg:
            numOrgs += 1
            allContributors.append(newOrg)
        if 'ExpenditureIDs' in oldOrg or 'ReceiptIDs' in oldOrg: 
            numOrgs += 1
            allPayees.append(newOrg)
    print('>> Loaded ' + str(numOrgs) + ' organizations from ' + GEOCODING + '.')

def locateContributorsAndPayees():
    global allContributors
    global allPayees
    # load state geojson
    with (open('../data/map/' + STATE_FILE)) as f:
        s = json.load(f)
    stateShape = shape(s['features'][0]['geometry'])
    # load counties geojson
    with (open('../data/map/' + COUNTIES_FILE)) as f:
        c = json.load(f)
    Counties = {}
    for county in c['features']:
        Counties[county['properties']['name']] = shape(county['geometry'])
    # load senate districts geojson
    with (open('../data/map/' + UPPER_DISTRICTS)) as f:
        u = json.load(f)
    senateDistricts = {}
    for district in u['geometries']:
        senateDistricts[district['district']] = shape(district)
    # load house districts geojson
    with (open('../data/map/' + LOWER_DISTRICTS)) as f:
        l = json.load(f)
    houseDistricts = {}
    for district in l['geometries']:
        houseDistricts[district['district']] = shape(district)
    # for each entity with coordinates, try to locate them
    modifiedRecords = 0
    for entityList in (allContributors, allPayees):
        for entity in entityList:
            if 'geo_data' in entity:
                modifiedRecords += 1
                entity['in_state'] = 0
                thisPoint = Point(entity['geo_data'][0], entity['geo_data'][1])
                if stateShape.contains(thisPoint): 
                    entity['in_state'] = 1
                    for countyName in Counties:
                        if Counties[countyName].contains(thisPoint):
                            entity['county'] = countyName
                            break
                    for senateDistrictName in senateDistricts:
                        if senateDistricts[senateDistrictName].contains(thisPoint):
                            entity['senate_district'] = senateDistrictName[16:]
                            break
                    for houseDistrictName in houseDistricts:
                        if houseDistricts[houseDistrictName].contains(thisPoint):
                            entity['house_district'] = houseDistrictName[15:]
                            break
    print('>> Modified ' + str(modifiedRecords) + ' records with location data.')

if __name__=='__main__':
    main() 
