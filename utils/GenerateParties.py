#!/usr/bin/python3

###################################################################
#
# File: GenerateParties.py
# Last Edit: 2015-03-10
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: This script reads the data files from alabamavotes.gov
# and finds all the unique organizations (PACs & Candidates).
# It also reads the Party information from that site, and
# cross-references it with the existing data. Finally, it 
# makes requests to Google's Civic Information API 
# for things like contact info and photos, and adds that data.
# If you want to run this, make sure to get an API key from 
# your Google Developers Console and put it in the constant below.
# Also be aware of the API usage limits.
# For Google's documentation, see:
# https://developers.google.com/civic-information/docs/v2
# This makes use of Open Civic Data IDs:
# http://opencivicdata.readthedocs.org/en/latest/ocdids.html
# It can output Party data either in JSON or CSV format.
# It also writes API responses to a file in case you have to 
# run this multiple times due to request limits or errors.
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
from time import sleep
from operator import itemgetter

# 3rd party libraries
from fuzzywuzzy import fuzz
from nameparser import HumanName
from numpy import mean

# constants
DATAFILES = ['2014_CashContributionsExtract_fixed.csv',
             '2014_ExpendituresExtract_fixed.csv',
             '2014_InKindContributionsExtract.csv',
             '2014_OtherReceiptsExtract.csv']
PARTYINFO = ['2014_Parties_active_fixed.csv', '2014_Parties_dissolved.csv']
OCDIDS = os.listdir('../data/ocdIDs/')
CACHEFILE = '.API_Responses_cache.json'
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://www.googleapis.com/civicinfo/v2/representatives/'
REQUEST_LIMIT = 25000
OUTFILE = '2014_Parties' # file extension will be added
HEADERS = ['name', '_id', 'type', 'status', 'party', 'office', 'district', 'place', 'phone', 'email', 'url', 'photoURL', 'facebookID', 'twitterID']
OUTPUT_JSON = False # otherwise CSV
PRETTY_PRINT = True # controls whitespace in JSON
OUTFILENAME = OUTFILE + ('.json' if OUTPUT_JSON else '.csv')

def main():
    global allParties
    allParties = [] # all PACs and Candidates
    global allOrgIDs
    allOrgIDs = [] # used to ensure we don't have duplicates
    # start by finding all unique organizations (by id) and adding them to allParties
    for filename in DATAFILES:
        with open('../data/' + filename, 'r', errors='replace', newline='') as csvfile:
            findUniqueOrgs(csv.reader(csvfile))
    # add the info we have on each candidate from the Parties files
    for filename in PARTYINFO:
        with open('../data/' + filename) as datafile:
            addPartyInfo(csv.reader(datafile))    
    global allOCDIDs
    allOCDIDs = []
    # pull the OpenCivicData IDs into memory
    for filename in OCDIDS:
        with open('../data/ocdIDs/' + filename) as datafile:
            allOCDIDs += csv.reader(datafile)
    global allResponses
    allResponses = {} # to save responses we get from Google
    # check if there's any cached data from a previous run
    try:
        with open(CACHEFILE) as datafile:
            allResponses = json.load(datafile)
    except FileNotFoundError:
        pass
    # make API requests to Google for candidate info
    makeAPIRequests()
    print('>> Writing party data to ' + OUTFILENAME + '.')
    if OUTPUT_JSON:
        with open('../data/' + OUTFILENAME, 'w') as datafile:
            if PRETTY_PRINT:
                json.dump(allParties, datafile, sort_keys=True, 
                          indent=4, separators=(',', ': '))
            else:
                json.dump(allParties, datafile)
    else: # output CSV
        with open('../data/' + OUTFILENAME, 'w', newline='') as datafile:
            writer = csv.DictWriter(datafile, quoting=csv.QUOTE_ALL, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(allParties)
    print('>> Writing a copy of API responses to ' + CACHEFILE + '.')
    with open(CACHEFILE, 'w') as datafile:
        json.dump(allResponses, datafile) # just in case we need them

def findUniqueOrgs(records):
    global allParties
    global allOrgIDs
    # iterate over the records looking for new information
    for i, record in enumerate(records):
        if i == 0:
            OrgIDColumn = record.index('OrgID')
            CommitteeTypeColumn = record.index('CommitteeType')
            CommitteeNameColumn = record.index('CommitteeName')
            CandidateNameColumn = record.index('CandidateName')
        else:
            # if it's a new OrgID, gather the info
            if record[OrgIDColumn] not in allOrgIDs:
                allOrgIDs.append(record[OrgIDColumn])
                thisOrg = {} 
                thisOrg['_id'] = record[OrgIDColumn]
                if record[CommitteeTypeColumn] == 'Political Action Committee':
                    thisOrg['type'] = 'PAC'
                elif record[CommitteeTypeColumn] == 'Principal Campaign Committee':
                    thisOrg['type'] = 'Candidate'
                else:
                    print('>> Error: Unknown group type: ' + record[CommitteeTypeColumn])
                    print('>> Quitting')
                    sys.exit(1)
                if len(record[CommitteeNameColumn]) > 1:
                    rawName = record[CommitteeNameColumn]
                    # fix capitalization
                    thisOrg['name'] = rawName.title().replace('Pac', 'PAC').replace('"', '').strip()
                else:
                    rawName = record[CandidateNameColumn]
                    thisOrg['name'] = rawName.title().replace('Ii', 'II').replace('Iii', 'III').replace('"', '').strip()
                allParties.append(thisOrg)

def addPartyInfo(records):
    # iterate over the records and add the info to allParties
    for i, record in enumerate(records):
        if i == 0:
            CandidateNameCol = record.index('CandidateName')
            PartyCol = record.index('Party')
            OfficeCol = record.index('Office')
            DistrictCol = record.index('District')
            PlaceCol = record.index('Place')
            CommitteeStatusCol = record.index('CommitteeStatus')
            CommitteeIDCol = record.index('CommitteeID')
        else:
            # if the ID is in the data, add to it
            for party in allParties:
                if party['_id'] == record[CommitteeIDCol]:
                    party['name'] = record[CandidateNameCol]
                    party['party'] = record[PartyCol]
                    party['office'] = record[OfficeCol]
                    if len(record[DistrictCol]) > 0: 
                        party['district'] = record[DistrictCol]
                    if len(record[PlaceCol]) > 0:
                        party['place'] = record[PlaceCol]
                    party['status'] = record[CommitteeStatusCol]
                    break # don't waste time looking for another match

# make calls to makeAPIRequest(ocdID)
def makeAPIRequests():
    numFailures = 0
    numRequests = 0
    # make an API request for each OCD ID
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

# process the reply we received, looking for officials in our database
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
            try:
                originalParty = official['party']
                normalParty = ('Democrat' if originalParty == 'Democratic' else originalParty)
                official['party'] = normalParty # so we scrape the formatted version
            except KeyError:
                normalParty = ''
            try:
                officialPhone = official['phones'][0]
            except KeyError:
                officialPhone = ''
            try:
                officialEmail = official['emails'][0]
            except KeyError:
                officialEmail = ''
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
                scrapeData(official, bestOrgID)
    return True

# scrape whatever useful data we can from the reply
def scrapeData(official, candidateOrgID):
    for party in allParties:
        if party['_id'] == candidateOrgID:
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
