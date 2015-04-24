#!/usr/bin/python3

###################################################################
#
# File: CallCivicInfoAPI.py
# Author: Matthew Leeds <mwl458@gmail.com>
# License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
# Purpose: This script reads the output from GenerateParties.py
# and makes calls to Google's Civic Information API for more
# information (contact info, photo URL, etc.). This is added to
# the existing data.
# If you want to run this, make sure to get an API key from 
# your Google Developers Console and put it in the constant below.
# Also be aware of the API usage limits.
# For Google's documentation, see:
# https://developers.google.com/civic-information/docs/v2
# This makes use of Open Civic Data IDs:
# http://opencivicdata.readthedocs.org/en/latest/ocdids.html
# It also writes API responses to a file in case you have to 
# run this multiple times due to request limits or errors.
# Configuration parameters are read from 'config.ini'.
# 
###################################################################

# system libraries
import os
import traceback
import json
import csv
from sys import exit
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.error import HTTPError
from time import sleep, time
from operator import itemgetter
from configparser import ConfigParser

# 3rd party libraries
from fuzzywuzzy import fuzz
from nameparser import HumanName
from numpy import mean

def main():
    global config
    config = ConfigParser()
    config.read('config.ini')
    if len(config.get('CALL_CIVICINFO', 'API_KEY')) == 0:
        print('>> You must specify an API key in the config file to use the Google Civic Info API!')
        exit(1)
    DATA_DIR = config.get('CALL_CIVICINFO', 'DATA_DIR')
    CACHEFILE = config.get('CALL_CIVICINFO', 'CACHEFILE')
    PARTIES_FILE = config.get('GENERATE_PARTIES', 'OUTFILE')
    DISTRICTS_FILE = config.get('GENERATE_DISTRICTS', 'OUTFILE')
    PRETTY_PRINT = config.getboolean('CALL_CIVICINFO', 'PRETTY_PRINT')
    global allParties
    allParties = [] # all PACs and Candidates
    try:
        with open(DATA_DIR + PARTIES_FILE) as datafile:
            print('>> Loading data from ' + PARTIES_FILE + '...', end='')
            allParties = json.load(datafile)
    except FileNotFoundError:
        print('>> ' + PARTIES_FILE + ' not found! You should run GenerateParties.py.')
        exit(1)
    print(str(len(allParties)) + ' records loaded.')
    global allDistricts
    allDistricts = []
    try:
        with open(DATA_DIR + DISTRICTS_FILE) as datafile:
            print('>> Loading data from ' + DISTRICTS_FILE + '...', end='')
            allDistricts = json.load(datafile)
    except FileNotFoundError:
        print('>> ' + DISTRICTS_FILE + ' not found! You should run GenerateDistricts.py.')
        exit(1)
    print(str(len(allDistricts)) + ' records loaded.')
    # Remove OCD IDs for which we already have recent data.
    removeUsedIDs()
    global allResponses
    allResponses = {} # to save responses we get from Google
    # check if there's any cached data from a previous run
    try:
        with open(DATA_DIR + CACHEFILE) as datafile:
            print('>> Loading cached API responses.')
            allResponses = json.load(datafile)
    except FileNotFoundError:
        pass
    # make API requests to Google for candidate info
    print('>> Starting API calls to Google.')
    success = makeAPIRequests()
    print('>> Writing party data to ' + PARTIES_FILE)
    with open(DATA_DIR + PARTIES_FILE, 'w') as datafile:
        if PRETTY_PRINT:
            json.dump(allParties, datafile, sort_keys=True, 
                      indent=4, separators=(',', ': '))
        else:
            json.dump(allParties, datafile)
    print('>> Writing a copy of API responses to ' + CACHEFILE)
    with open(DATA_DIR + CACHEFILE, 'w') as datafile:
        json.dump(allResponses, datafile) # just in case we need them
    if not success: exit(1)

# removes OCD IDs for which we already have fresh data
def removeUsedIDs():
    global config
    global allDistricts
    global allParties
    TTL_SECONDS = config.getint('CALL_CIVICINFO', 'TTL_SECONDS')
    for party in allParties:
        if party['API_status'] == 'OK' and (time() - party['API_timestamp']) < TTL_SECONDS:
            # iterate over a copy so we can delete some
            for district in list(allDistricts):
                if district['ocdID'] == party['ocdID']:
                    allDistricts.remove(district)
                    break

# make calls to makeAPIRequest(ocdID)
def makeAPIRequests():
    global config
    global allDistricts
    MAX_API_REQUESTS = config.getint('CALL_CIVICINFO', 'MAX_API_REQUESTS') 
    VERBOSE = config.getboolean('CALL_CIVICINFO', 'VERBOSE')
    numFailures = 0
    numRequests = 0
    success = True # return value
    # make an API request for each OCD ID if we don't already have the info
    for district in allDistricts:
        if numRequests == MAX_API_REQUESTS:
            print('>> Error: Configured API request limit reached (' + str(MAX_API_REQUESTS) + ').')
            success = False
            break
        if VERBOSE: 
            print('>> Requesting data for ' + district['name'])
        # catch any errors to ensure the data gets written to disk
        try:
            if not makeAPIRequest(district['ocdID']):
                numFailures += 1
            numRequests += 1
        except Exception as e:
            print('>> Caught Error: ' + str(e))
            traceback.print_exc()
            success = False
            break
    print('>> ' + str(numRequests) + ' requests made.')
    print('>> ' + str(numFailures) + ' requests failed.') 
    if not success: return False
    return (numFailures < numRequests)

# make a representativeInfoByDivision query to Google
def makeAPIRequest(ocdID):
    global config
    global allResponses
    BASE_URL = config.get('CALL_CIVICINFO', 'BASE_URL')
    API_KEY = config.get('CALL_CIVICINFO', 'API_KEY')
    # don't make the request again if we have it cached
    if ocdID in allResponses:
        reply = allResponses[ocdID]
    else:
        url = BASE_URL + quote_plus(ocdID) + '?key=' + API_KEY 
        try:
            response = urlopen(url)
        except:
            print('ocdID: ' + ocdID)
            print('URL: ' + url)
            raise
        sleep(0.1) # go easy on their servers
        rawReply = response.read()
        reply = json.loads(rawReply.decode('utf-8'))
        # save the response in case we need it later
        allResponses[ocdID] = reply
    # process the reply data
    processSuccess = processReply(reply, ocdID)
    return processSuccess

# process the reply we received, looking for matching officials in our data
def processReply(reply, ocdID):
    global allParties
    # we're about to use a lot of 'duct tape' to try to make Google's
    # data look more like our data
    try:
        offices = reply['offices']
    except KeyError:
       return False 
    divisionName = reply['divisions'][ocdID]['name']
    if 'Alabama State Senate district' in divisionName or \
        'Alabama State House district' in divisionName:
        divisionName = divisionName[14:].title() # normalize
    for office in offices:
        officeName = office['name']
        if 'AL State Senate District' in officeName:
            officeName = 'State Senator' # normalize
        elif 'AL State House District' in officeName:
            officeName = 'State Representative' # normalize
        for officialIndex in office['officialIndices']: 
            official = reply['officials'][officialIndex]
            originalName = HumanName(official['name'])
            normalName = str(originalName.last) + ', ' + str(originalName.first)
            official['name'] = normalName # so we scrape the formatted version
            normalParty, originalParty = '', ''
            # Don't fail when the data isn't there
            try:
                originalParty = official['party']
            except KeyError:
                pass
            normalParty = ('Democrat' if originalParty == 'Democratic' else originalParty)
            official['party'] = normalParty # so we scrape the formatted version
            officialPhone = ''
            try:
                officialPhone = official['phones'][0]
            except KeyError:
                pass
            officialEmail = ''
            try:
                officialEmail = official['emails'][0]
            except KeyError:
                pass
            # look for a matching person with an orgID
            possibleMatches = {}
            for party in allParties:
                if party['type'] == 'Candidate':
                    # how likely is it the returned person is the same as in the party data?
                    matchProbability = 0.0 # 100 = very likely match
                    # try to match on name, party, office, phone, email, and district
                    # I wonder if we should weight these by different amounts using coefficients?
                    matchingRatios = []
                    # weight name similarities heavily b/c different people run for the same office
                    matchingRatios.append(fuzz.ratio(party['name'], normalName))
                    matchingRatios.append(fuzz.ratio(party['name'], normalName))
                    if 'party' in party:
                        matchingRatios.append(fuzz.ratio(party['party'], normalParty))
                    if 'office' in party:
                        matchingRatios.append(fuzz.ratio(party['office'], officeName))
                    if 'phone' in party:
                        matchingRatios.append(fuzz.ratio(party['phone'], officialPhone))
                    if 'email' in party:
                        matchingRatios.append(fuzz.ratio(party['email'], officialEmail))
                    if 'district' in party:
                        matchingRatios.append(fuzz.ratio(party['district'], divisionName))
                    # take a simple average
                    matchProbability = mean(matchingRatios)
                    if matchProbability > 90: # arbitrary minimum threshold
                        possibleMatches[party['ID']] = matchProbability
            if len(possibleMatches) == 0:
                continue # to next official
            else:
                # find the orgID with the highest matchProbability
                bestOrgID = max(possibleMatches.items(), key=itemgetter(1))[0]
                # add useful info about that official to our database
                scrapeData(official, bestOrgID, ocdID)
    return True

# scrape whatever useful data we can from the reply
def scrapeData(official, candidateOrgID, ocdID):
    global allParties
    for party in allParties:
        if party['ID'] == candidateOrgID:
            party['API_status'] = 'OK'
            party['API_timestamp'] = int(time())
            party['ocdID'] = ocdID
            try:
                party['party'] = official['party']
            except KeyError:
                pass
            try:
                party['phone'] = official['phones'][0]
            except KeyError:
                pass
            try:
                party['email'] = official['emails'][0]
            except KeyError:
                pass
            try:
                party['url'] = official['urls'][0]
            except KeyError:
                pass
            try:
                party['photoURL'] = official['photoUrl']
            except KeyError:
                pass
            try:
                for channel in official['channels']:
                    if channel['type'] == 'Facebook':
                        party['facebookID'] = channel['id']
                    elif channel['type'] == 'Twitter':
                        party['twitterID'] = channel['id']
            except KeyError:
                pass
            break

if __name__=='__main__':
    main()
