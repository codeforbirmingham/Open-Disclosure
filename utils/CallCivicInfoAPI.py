#!/usr/bin/python3

###################################################################
#
# File: CallCivicInfoAPI.py
# Last Edit: 2015-03-17
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
# 
# This script requires Python 3.4 or later.
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
from contextlib import suppress

# 3rd party libraries
from fuzzywuzzy import fuzz
from nameparser import HumanName
from numpy import mean

# constants
OCDIDS = os.listdir('../data/ocdIDs/')
CACHEFILE = '.API_Responses_cache.json'
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://www.googleapis.com/civicinfo/v2/representatives/'
REQUEST_LIMIT = 25000
TTL_SECONDS = 30 * 24 * 60 * 60 # API responses expire after 30 days
PARTIES_FILE = '2014_Parties.json'
PRETTY_PRINT = True # controls whitespace in JSON

def main():
    global allParties
    allParties = [] # all PACs and Candidates
    print('>> Loading data from ' + PARTIES_FILE + '...', end='')
    with open('../data/' + PARTIES_FILE) as datafile:
        allParties = json.load(datafile)
    print(str(len(allParties)) + ' records loaded.')
    global allOCDIDs
    allOCDIDs = []
    # pull the OpenCivicData IDs into memory
    for filename in OCDIDS:
        with open('../data/ocdIDs/' + filename) as datafile:
            allOCDIDs += csv.reader(datafile)
    removeUsedIDs()
    global allResponses
    allResponses = {} # to save responses we get from Google
    # check if there's any cached data from a previous run
    try:
        with open(CACHEFILE) as datafile:
            allResponses = json.load(datafile)
    except FileNotFoundError:
        pass
    # make API requests to Google for candidate info
    print('>> Starting API calls to ' + BASE_URL + '.')
    makeAPIRequests()
    print('>> Writing party data to ' + PARTIES_FILE + '.')
    with open('../data/' + PARTIES_FILE, 'w') as datafile:
        if PRETTY_PRINT:
            json.dump(allParties, datafile, sort_keys=True, 
                      indent=4, separators=(',', ': '))
        else:
            json.dump(allParties, datafile)
    print('>> Writing a copy of API responses to ' + CACHEFILE + '.')
    with open(CACHEFILE, 'w') as datafile:
        json.dump(allResponses, datafile) # just in case we need them

# removes OCD IDs for which we already have fresh data
def removeUsedIDs():
    global allOCDIDs
    global allParties
    for party in allParties:
        if party['_API_status'] == 'OK' and (time() - party['_API_timestamp']) < TTL_SECONDS:
            for ocdRecord in allOCDIDs:
                if ocdRecord[0] == party['ocdID']:
                    allOCDIDs.remove(ocdRecord)
                    break

# make calls to makeAPIRequest(ocdID)
def makeAPIRequests():
    numFailures = 0
    numRequests = 0
    # make an API request for each OCD ID if we don't already have the info
    for ocdRecord in allOCDIDs:
        if numRequests == REQUEST_LIMIT:
            print('>> Error: Usage quota reached (' + str(REQUEST_LIMIT) + ').')
            break
        print('>> Requesting data for ' + ocdRecord[1])
        # catch any errors to ensure the data gets written to disk
        try:
            if not makeAPIRequest(ocdRecord[0]):
                numFailures += 1
            numRequests += 1
        except Exception as e:
            print('>> Caught Error: ' + str(e))
            traceback.print_exc()
            break
    print('>> ' + str(numRequests) + ' requests made.')
    print('>> ' + str(numFailures) + ' requests failed.') 

# make a representativeInfoByDivision query to Google
def makeAPIRequest(ocdID):
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
            # Don't fail when the data isn't there
            with suppress(KeyError):
                normalParty, originalParty = '', ''
                originalParty = official['party']
                normalParty = ('Democrat' if originalParty == 'Democratic' else originalParty)
                official['party'] = normalParty # so we scrape the formatted version
                officialPhone = ''
                officialPhone = official['phones'][0]
                officialEmail = ''
                officialEmail = official['emails'][0]
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
                        possibleMatches[party['_id']] = matchProbability
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
    for party in allParties:
        if party['_id'] == candidateOrgID:
            with suppress(KeyError):
                party['_API_status'] = 'OK'
                party['_API_timestamp'] = int(time())
                party['ocdID'] = ocdID
                party['party'] = official['party']
                party['phone'] = official['phones'][0]
                party['email'] = official['emails'][0]
                party['url'] = official['urls'][0]
                party['photoURL'] = official['photoUrl']
                for channel in official['channels']:
                    if channel['type'] == 'Facebook':
                        party['facebookID'] = channel['id']
                    elif channel['type'] == 'Twitter':
                        party['twitterID'] = channel['id']
            break

if __name__=='__main__':
    main()
