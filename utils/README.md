# Open-Disclusure/utils #
This is a collection of Python scripts that download, organize, and enhance data from alabamavotes.gov. They've all been written with a focus on readability over efficiency, so keep that in mind if you contribute.

## System Requirements ##
* Python 3.4 or later
* a Linux environment (OS X or Windows may work)
* Python libraries: shapely, fuzzywuzzy, nameparser, numpy, selenium

## High-level Overview ##
Here is a brief description of the scripts which are separated into categories based on when they should be run. With the exception of GenerateTransactions.py, scripts within a step can be run in any order.

### Step 1: Download the Data ###
* DataFetcher.py: This downloads the four main CSV files (CashContributions, InKindContributions, Expenditures, OtherReceipts) with all the campaign finance data. That data is updated every 24 hours.
* PartyFetcher.py: This downloads two CSV files which have information for "Active" and "Dissolved" parties (political candidates).

### Step 2: Organize the Data ###
* GenerateContributorsAndPayees.py: This looks at the four data files and identifies all the people transacting with the PACs and Candidates. For Expenditures, these are referred to as Payees. For all the other data files, they are referred to as Contributors.
* GenerateParties.py: This looks at all the data files including the Parties and finds all the unique PACs and Candidates (using their OrgIDs).
* GenerateTransactions.py: This looks at the four data files and records every transaction. **This has to be run after GenerateContributorsAndPayees.py.**
* GenerateDistricts.py: This looks at the Open Civic Data IDs in /data/ocdIDs/ and puts that in JSON format (matching each ID to its friendly name).

### Step 3: Add to the Data ###
* CallGeocodingAPI.py: This calls Google's Geocoding API to convert street addresses to coordinates for all the contributors and payees, and locates them by district, county, etc. using the files in /data/map/.
* CallCivicInfoAPI.py: This calls Google's Civic Information API to get information on each OCD ID in Alabama, adding to the existing data.

### Step 4: Send the Data to Socrata ###
Coming Soon...

## Next Steps ##
At this point we need to do a lot of testing to ensure the scripts do what we think they do. Then we can upload the data to Socrata so we have an API for our frontend (and anyone else with a use for it).

## Copyleft ##
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
