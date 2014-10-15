#!/usr/bin/python3

############################################################################
#
# File: GeocodeData.py
# Last Edit: 10.15.2014
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: This script reads the four CSV files from
# http://fcpa.alabamavotes.gov/PublicSite/DataDownload.aspx
# and sends the addresses of each contributor/payee to the 
# Google Maps API for geocoding (conversion to lat/long coords).
# The output is YEAR_Geocoding.json in the format:
# {"Organization Name": {"_id": 123456,
#                        "orgType": "Individual/PAC/Business",
#                        "addr": "Street address",
#                        "coords": {'lat': -123, 'lng': 456},
#                        "ReceiptIDs": [txID, ...],
#                        "ExpenditureIDs": [txID, ...],
#                        "InKindContributionIDs": [txID, ...],
#                        "ContributionIDs": [txID, ...],
#                        "associatedWith": [orgID, ...]
#                        }, ...}
# The "orgType" field is from the "ReceiptSourceType" or "ContributorType"
# columns. The txIDs are the unique identifiers for rows in the data files,
# so either ReceiptID, ExpenditureID, InKindContributionID, or ContributionID
# depending on the file. They are only unique within their own file. 
# The orgIDs identify the relevant PAC or political candidate.
# The Google Maps API documentation is here:
# https://developers.google.com/maps/documentation/geocoding/
# You'll need to make a "Simple API key for server apps" here:
# https://code.google.com/apis/console/?noredirect
# 
# There's also a function, geocodeOSM, for using the OpenStreetMap.org API:
# http://wiki.openstreetmap.org/wiki/Nominatim
#
############################################################################


import csv
import json
from urllib.request import urlopen
from urllib.parse import urlencode
from time import sleep

# email address parameter for OSM
EMAIL_ADDRESS = 'YOUR_EMAIL'
# google API Key
API_KEY = 'YOUR_API_KEY'
MAX_API_REQUESTS = 2500 # per day
# an estimated minimum bounding rectangle around Alabama formatted for Google
ALABAMA_BOUNDS = '35.046674,-88.751659|30.077183,-84.687088'
# formatted for OSM
ALABAMA_BOUNDS_OSM = '-88.7,35.09,-84.79,30.06'
# file names
DATAFILES = ['2014_CashContributionsExtract_fixed.csv',
             '2014_ExpendituresExtract_fixed.csv',
             '2014_InKindContributionsExtract.csv',
             '2014_OtherReceiptsExtract.csv']
OUTFILE = '2014_Geocoding.json'
# the indices of important columns in the CSV files
COLUMN_INDICES = {'2014_CashContributionsExtract_fixed.csv': {'OrgID': 0, 'LastName': 3, 'Address': 7, 'txID': 11, 'orgType': 14},
                  '2014_ExpendituresExtract_fixed.csv': {'OrgID': 0, 'LastName': 3, 'Address': 7, 'txID': 12},
                  '2014_InKindContributionsExtract.csv': {'OrgID': 0, 'LastName': 3, 'Address': 7, 'txID': 11, 'orgType': 15},
                  '2014_OtherReceiptsExtract.csv': {'OrgID': 0, 'LastName': 3, 'Address': 7, 'txID': 11, 'orgType': 14}}
# it's not worth trying to geocode addresses containing these strings
BAD_ADDRESSES = ['NOT KNOWN', 'PO BOX', 'P.O. BOX', 'P O BOX', 'P. O. BOX', 'P.O.BOX', 'POST OFFICE BOX']


def main():
    global allOrganizations
    allOrganizations = {} # list of organizations with the associated data listed above
    # in case this is not the first run, load the output file 
    try:
        with open('../data/' + OUTFILE) as lastOutput:
            allOrganizations = json.load(lastOutput)
    except Exception:
        pass
    global maxID
    maxID = 0
    if len(allOrganizations) > 0:
        maxID = findMaxID(allOrganizations)
    global numAPIRequests
    numAPIRequests = 0 # keep track so we don't exceed usage limits
    for filename in DATAFILES:
        # for each file, process all the records
        with open('../data/' + filename, 'r', errors='ignore', newline='') as csvfile:
            try:
                if not process(csv.reader(csvfile), COLUMN_INDICES[filename]):
                    break # failure
            except Exception as e:
                print('Caught error:\n' + str(e))
                break
    # export the data in json format
    with open('../data/' + OUTFILE, 'w') as output:
        json.dump(allOrganizations, output) 

# find the max value for the '_id' field in the existing data
def findMaxID(allOrgs):
    currentMaxID = 0
    for key in allOrgs:
        if allOrgs[key]['_id'] > currentMaxID:
            currentMaxID = allOrgs[key]['_id'] 
    return currentMaxID

# this goes through all the records and attempts to geocode them
def process(records, columnIndex):
    success = True # return value
    global allOrganizations
    global numAPIRequests
    # calculate columns (array indices) in the data
    orgIDCol = columnIndex['OrgID']
    lastNameCol = columnIndex['LastName']
    firstNameCol = columnIndex['LastName'] + 1
    MICol = columnIndex['LastName'] + 2
    suffixCol = columnIndex['LastName'] + 3
    addressCol = columnIndex['Address']
    cityCol = columnIndex['Address'] + 1
    stateCol = columnIndex['Address'] + 2
    zipCol = columnIndex['Address'] + 3
    txIDCol = columnIndex['txID']
    # not every data file has a ContributorType column
    try:
        orgTypeCol = columnIndex['orgType']
    except:
        orgTypeCol = -1
    # iterate over the records, geocoding the addresses of each contributing party
    # and noting which other transactons and orgID's they're associated with
    for i, record in enumerate(records):
        if i == 0: # column headers
            # determine if it's an ExpenditureID, ContributionID, etc.
            idColName = record[txIDCol] + 's'
            continue
        if numAPIRequests >= MAX_API_REQUESTS:
            print('Error: Exceeded Google Maps API Usage limits. Run this again in 24 hours.')
            success = False
            break
        name = record[lastNameCol] + ' ' + record[firstNameCol] + ' ' + record[MICol] + ' ' + record[suffixCol]
        name = name.strip().title() # so organizations don't have trailing spaces and aren't ALL CAPS
        address = record[addressCol] + ' ' + record[cityCol] + ' ' + record[stateCol] + ' ' + record[zipCol]
        address = address.strip()
        orgid = record[orgIDCol]
        txid = record[txIDCol]
        try:
            orgtype = record[orgTypeCol]
        except:
            orgtype = ''
        # if we already have this organization on record, update it
        if name in allOrganizations:
            try:
                existingIDs = allOrganizations[name][idColName]
            except:
                allOrganizations[name][idColName] = [txid]
                try:
                    (allOrganizations[name]['associatedWith']).append(orgid)
                except:
                    allOrganizations[name]['associatedWith'] = [orgid]
                existingIDs = [txid]
            if txid not in existingIDs: 
                (allOrganizations[name][idColName]).append(txid)
                if orgid not in allOrganizations[name]['associatedWith']:
                    (allOrganizations[name]['associatedWith']).append(orgid)
        # otherwise make a new record and geocode the address
        else:
            newOrg = {}
            # create a unique ID
            maxID += 1
            newOrg['_id'] = maxID
            newOrg['orgType'] = orgtype
            newOrg[idColName] = [txid]
            newOrg['associatedWith'] = [orgid]
            # if all goes well, the 'addr' and 'coords' fields will be overwritten
            newOrg['addr'] = address 
            newOrg['coords'] = ''
            # try to determine if it's worth geocoding
            if len(address) > 0 and checkString(address, BAD_ADDRESSES):
                print('Geocoding row ' + str(i) + ': ' + address)
                result = geocodeGoogle(address) # make the request to Google 
                #result = geocodeOSM(address) # make the request to OSM
                numAPIRequests += 1
                if isinstance(result, str):
                    print('Error: ' + result)
                    if result == 'REQUEST_DENIED' or result == 'OVER_QUERY_LIMIT':
                        success = False
                        break # give up
                else: # success
                    newOrg['addr'] = result[1] # nicely formatted address
                    # round coordinates to 6 decimal places (~0.1m precision)
                    newOrg['coords'] = {'lat': round(result[0]['lat'], 6),
                                        'lng': round(result[0]['lng'], 6)}
            allOrganizations[name] = newOrg
    return success

# uses the Google Maps API to geocode an address
# on success: returns a tuple with the coordinates and the formatted address
# on failure: returns the status code (a string)
def geocodeGoogle(address):
    # the bounds parameter biases results to locations within Alabama
    params = {'address': address, 
              'bounds': ALABAMA_BOUNDS,
              'key': API_KEY}
    url = 'https://maps.googleapis.com/maps/api/geocode/json?' + urlencode(params, safe='/,|')
    rawreply = urlopen(url).read()
    reply = json.loads(rawreply.decode('utf-8'))
    sleep(0.1) # stay under usage limit
    # assume the first result is correct
    if reply['status'] == 'OK':
        return (reply['results'][0]['geometry']['location'], reply['results'][0]['formatted_address'])
    else:
        return reply['status']

# uses the OpenStreetMap.org "Nominatim" geocoding service via MapQuest
# return values should match the format that the Google Maps function returns
def geocodeOSM(address):
    params = {'q': address,
              'format': 'json',
              'email': EMAIL_ADDRESS,
              'viewbox': ALABAMA_BOUNDS_OSM,
              'limit': '1',
              'addressdetails': '0'}
    url = 'http://open.mapquestapi.com/nominatim/v1/search.php?' + urlencode(params)
    rawreply = urlopen(url).read()
    reply = json.loads(rawreply.decode('utf-8'))
    sleep(1)
    try:
        coords = {'lat': reply[0]['lat'], 'lng': reply[0]['lon']}
        niceAddress = reply[0]['display_name']
        result = (coords, niceAddress)
    except:
        result = 'NO_RESULTS_FOUND'
    return result

# takes in a string and a blacklist and returns false if there are any matches
def checkString(string, blacklist):
    isGood = True
    for phrase in blacklist:
        if phrase in string:
            isGood = False
            break
    return isGood

if __name__=='__main__':
    main()
