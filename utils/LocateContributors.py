#!/usr/bin/python

##############################################################################
#
# File: LocateContributors.py
# Last Edit: 10.14.2014
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: Read in the "2014_Geocoding.json" file (produced by GeocodeData.py)
# and for each entity with geographic coordinates, determine if they're 
# in-state, which county they're in, and which house and senate district 
# they're in. This information is then outputted to 
# "2014_ContributorLocations.json" in the format:
# {"_id": { "geo_data": [long, lat], 
#           "inState": 0|1,
#           "county": "County Name",
#           "senate": "District Number",
#           "house": "District Number"
#          }, ...}
# Dependencies: shapely (which depends on the 'libgeos-dev' package)
#
##############################################################################

import json
from shapely.geometry import Point, shape

GEOCODING_FILENAME = '2014_Geocoding.json'
OUT_FILE = '2014_ContributorLocations.json'
STATE_FILE = 'AL.geojson'
COUNTIES_FILE = 'AL_Counties.geojson'
UPPER_DISTRICTS = 'sldu-simple.json'
LOWER_DISTRICTS = 'sldl-simple.json'

def main():
    results = {}
    # load geographic coordinates
    with (open('../data/' + GEOCODING_FILENAME)) as f:
        g = json.load(f)
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
    for entity in g:
        if len(g[entity]['coords']) > 0:
            newEntity = {'inState': 0}
            newEntity['geo_data'] = [round(g[entity]['coords']['lng'], 6), round(g[entity]['coords']['lat'], 6)]
            thisPoint = Point(newEntity['geo_data'][0], newEntity['geo_data'][1])
            if stateShape.contains(thisPoint): 
                newEntity['inState'] = 1
                for countyName in Counties:
                    if Counties[countyName].contains(thisPoint):
                        newEntity['county'] = countyName
                        break
                for senateDistrictName in senateDistricts:
                    if senateDistricts[senateDistrictName].contains(thisPoint):
                        newEntity['senate'] = senateDistrictName[16:]
                        break
                for houseDistrictName in houseDistricts:
                    if houseDistricts[houseDistrictName].contains(thisPoint):
                        newEntity['house'] = houseDistrictName[15:]
                        break
            results[g[entity]['_id']] = newEntity
    with (open('../data/' + OUT_FILE, 'w')) as f:
        json.dump(results, f, sort_keys=True, indent=4, separators=(',', ': '))

if __name__=='__main__':
    main()
