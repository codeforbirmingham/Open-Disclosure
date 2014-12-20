#!/usr/bin/python3

###################################################################
#
# File: GetCandidateInfo.py
# Last Edit: 2014-12-19
# Author: Matthew Leeds <mwl458@gmail.com>
# Purpose: This script reads the PartyCollection.json file and 
# makes requests to Google's Civic Information API for more 
# information on the candidates, like contact info and photos.
# If you want to run this, make sure to get an API key from 
# your Google Developers Console and put it in the constant below.
# For Google's documentation, see:
# https://developers.google.com/civic-information/docs/v2
# This also makes use of Open Civic Data IDs:
# http://opencivicdata.readthedocs.org/en/latest/ocdids.html
#
###################################################################

import json
from urllib.request import urlopen
from urllib.parse import quote_plus
from time import sleep

PARTYFILE = '2014_PartyCollection.json'
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://www.googleapis.com/civicinfo/v2/representatives/'

def main():
    global allParties
    allParties = [] # all PACs and Candidates
    # pull the data into memory
    with open('../data/import/' + PARTYFILE) as datafile:
        allParties = json.load(datafile)
    makeAPIrequests()
    # write the data back out to the same file
    with open('../data/import/' + PARTYFILE, 'w') as datafile:
        json.dump(allParties, datafile, sort_keys=True, 
                  indent=4, separators=(',', ': '))

def makeAPIrequests():
    # for AL Congresspeople, make API requests
    for party in allParties:
        if party['type'] == 'Candidate': 
            if 'district' in party and 'District' in party['district']:
                ocdID = 'ocd-division/country:us/state:al/'
                if 'House' in party['district']:
                    ocdID += 'sldl:' + party['district'][15:]
                elif 'Senate' in party['district']:
                    ocdID += 'sldu:' + party['district'][16:]
                else:
                    print('>> Error: can\'t understand district ' + party['district'])
                    continue
                print('>> Requesting info for ' + party['name'])
                url = BASE_URL + quote_plus(ocdID) + '?key=' + API_KEY 
                # we're ready to make the request   
                response = urlopen(url)
                if response.getcode() == 200:
                    rawReply = response.read()
                else:
                    print('>> Error: Bad reply from Google. Status: ' + response.getcode())
                    break
                reply = json.loads(rawReply.decode('utf-8'))
                # go easy on their servers
                sleep(0.5)
                # process data 
                try:
                    candidateInfo = reply['officials'][0]
                except KeyError:
                    print('>> Error: No officials found for ' + party['name'])
                    print(reply)
                    break
                # don't fail on fields that aren't there
                try:
                    party['phone'] = candidateInfo['phones'][0]
                except KeyError:    
                    pass
                try:
                    party['url'] = candidateInfo['urls'][0]
                except KeyError:    
                    pass
                try:
                    party['photoURL'] = candidateInfo['photoUrl']
                except KeyError:    
                    pass
                try:
                    party['email'] = candidateInfo['emails'][0]
                except KeyError:    
                    pass
                try:
                    for channel in candidateInfo['channels']:
                        if channel['type'] == 'Facebook':
                            party['facebookID'] = channel['id']
                        elif channel['type'] == 'Twitter':
                            party['twitterID'] = channel['id']
                except KeyError:    
                    pass

if __name__=='__main__':
    main()
