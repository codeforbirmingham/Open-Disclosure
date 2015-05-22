# Makefile to automate downloading campaign finance data and processing it.
# Due to usage limits, automating Geocoding API calls is a little more complicated.

py = python3

all: download organize enhance flatten

download:
	$(py) DataFetcher.py
	$(py) PartyFetcher.py

organize:
	$(py) GenerateTransactees.py
	$(py) GenerateParties.py
	$(py) GenerateTransactions.py
	$(py) GenerateDistricts.py

enhance:
	$(py) CallCivicInfoAPI.py
  
flatten:
	$(py) FlattenData.py

clean:
	-rm data/*.json data/*.csv

.PHONY: all download organize enhance flatten clean
