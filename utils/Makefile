# Makefile to automate downloading campaign finance data and processing it.
# Due to usage limits, automating API calls is a little more complicated.

py = python3

all: download organize

.PHONY: all download organize clean

download:
	$(py) DataFetcher.py
	$(py) PartyFetcher.py

organize:
	$(py) GenerateTransactees.py
	$(py) GenerateParties.py
	$(py) GenerateTransactions.py
	$(py) GenerateDistricts.py

clean:
	-rm data/*.json data/*.csv
