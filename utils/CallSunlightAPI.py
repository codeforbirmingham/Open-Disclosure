#!/usr/bin/python3

__authors__ = 'cfilby, mleeds95'

import configparser
import sunlight
import json

class CallSunlightAPI:
    """
    Class responsible for fetching state specific Sunlight API Data.
    API Key is found in ~/.sunlight.key, Environment SUNLIGHT_API_KEY, or sunlight.config.api_key
    """

    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.state_code = self.config['SUNLIGHT']['STATE_CODE']
        self.pretty_print = self.config['SUNLIGHT']['PRETTY_PRINT']
        self.data_dir = self.config['SUNLIGHT']['DATA_DIR']
        self.parties_file = self.config['GENERATE_PARTIES']['OUTFILE']

    def fetchData(self):
        """Make various calls to Sunlight APIs."""
        #self.federal_legislators = sunlight.congress.legislators(state=self.state_code)
        self.state_legislators = sunlight.openstates.legislators(state=self.state_code)
        #self.state_bills = sunlight.openstates.bills(state=self.state_code)
        #self.state_districts = sunlight.openstates.districts(self.state_code.lower())
        #self.state_committees = sunlight.openstates.committees(state=self.state_code)

    def writeData(self):
        """Write the data returned to the disk."""
        with open(self.data_dir + 'StateLegislators.json', 'w') as f:
            if self.pretty_print:
                json.dump(self.state_legislators, f, indent=4, sort_keys=True, separators=(',', ': '))
            else:
                json.dump(self.state_legislators, f)
        with open(self.data_dir + 'StateBills.json', 'w') as f:
            if self.pretty_print:
                json.dump(self.state_bills, f, indent=4, sort_keys=True, separators=(',', ': '))
            else:
                json.dump(self.state_bills, f)
        with open(self.data_dir + 'StateDistricts.json', 'w') as f:
            if self.pretty_print:
                json.dump(self.state_districts, f, indent=4, sort_keys=True, separators=(',', ': '))
            else:
                json.dump(self.state_districts, f)
        with open(self.data_dir + 'StateCommittees.json', 'w') as f:
            if self.pretty_print:
                json.dump(self.state_committees, f, indent=4, sort_keys=True, separators=(',', ': '))
            else:
                json.dump(self.state_committees, f)

    def processData(self):
        """Integrate the data into the party and district data we already have."""
        allParties = []
        try:
            with open(self.data_dir + self.parties_file) as f:
                allParties = json.load(f)
        except FileNotFoundError:
            print('>> Error: ' + self.parties_file + ' not found! Run GenerateParties.py')
            return
        # Look for matching parties in the existing data.
        numModified = 0
        for legislator in self.state_legislators:
            district = ('HOUSE' if legislator['chamber'] == 'lower' else 'SENATE')
            district += ' DISTRICT ' + legislator['district']
            for party in allParties:
                if 'district' in party and party['district'] == district:
                    numModified += 1
                    # Copy some useful info from the Sunlight data (if it's there).
                    party['openstates_id'] = legislator['leg_id']
                    try:
                        party['office_address'] = legislator['office_address']
                    except KeyError:
                        pass
                    try:
                        party['phone'] = legislator['office_phone']
                    except KeyError:
                        pass
                    try:
                        party['email'] = legislator['email']
                    except KeyError:
                        pass
                    try:
                        party['url'] = legislator['url']
                    except KeyError:
                        pass
                    try:
                        party['photoURL'] = legislator['photo_url']
                    except KeyError:
                        pass
                    try:
                        party['influenceexplorer_id'] = legislator['transparencydata_id']
                    except KeyError:
                        pass
                    break # move on to the next legislator
        print('>> Modified ' + str(numModified) + ' party records with additional info.')
        print('>> Writing ' + str(len(allParties)) + ' records to ' + self.parties_file)
        with open(self.data_dir + self.parties_file, 'w') as f:
            if self.pretty_print:
                json.dump(allParties, f, indent=4, sort_keys=True, separators=(',', ': '))
            else:
                json.dump(allParties, f)

def main():
    callSunlight = CallSunlightAPI('config.ini')
    callSunlight.fetchData()
    #callSunlight.writeData()
    callSunlight.processData()

if __name__ == '__main__':
    main()
