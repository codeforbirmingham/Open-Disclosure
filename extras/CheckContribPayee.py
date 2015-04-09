# checks if contributors and payees and mutually exclusive in 2014_Geocoding.json

import json

j = json.load(open('../data/2014_Geocoding.json'))

numContrib = 0
numPayee = 0
for entity in j:
    contrib = False
    payee = False
    if 'ContributionIDs' in j[entity] or 'InKindContributionIDs' in j[entity]:
        contrib = True
        numContrib += 1
    if 'ExpenditureIDs' in j[entity] or 'ReceiptIDs' in j[entity]:
        payee = True
        numPayee += 1
    if contrib and payee:
        print('>> Found a dupe: ')
        print(entity)
print('>> ' + str(numContrib) + ' contributors and ' + str(numPayee) + ' payees found.')
