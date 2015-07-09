# Makefile to automate downloading campaign finance data and processing it.
# Due to usage limits, automating API calls is a little more complicated.

py = python3

all: download organize merge flatten

download:
	$(py) DataFetcher.py
	$(py) PartyFetcher.py

organize:
	$(py) GenerateDistricts.py
	$(py) GenerateTransactees.py
	$(py) GenerateParties.py
	$(py) GenerateTransactions.py

enhance:
	$(py) CallSunlightAPI.py

merge:
	$(py) CompareYears.py

flatten:
	$(py) FlattenData.py

upload:
	$(py) SendToSocrata.py

clean:
	-rm data/*.json data/*.csv

.PHONY: all download organize enhance merge flatten upload clean
