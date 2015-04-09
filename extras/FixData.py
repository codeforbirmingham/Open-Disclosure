#!/usr/bin/python3

# reads in "2014_Geocoding.json" and runs .title() on all the names, 
# and removes duplicates from the lists of txIDs and orgIDs

import json

def main():
    f = open('../data/2014_Geocoding.json')
    j = json.load(f)
    newJ = {}
    for key in j.keys():
        '''
        newkey = key.title()
        newLength = len(j[key]['txIDs'])
        try:
            oldLength = len(newJ[newkey]['txIDs']) 
        except:
            oldLength = 0
        if newLength >= oldLength:
            newJ[newkey] = j[key]
            newJ[newkey]['txIDs'] = uniq(newJ[newkey]['txIDs'])
            newJ[newkey]['contribTo'] = uniq(newJ[newkey]['contribTo'])
        '''
        temp = j[key]
        temp.pop('txIDs')
        temp.pop('contribTo')
        newJ[key] = temp
    json.dump(newJ, open('../data/2014_Geocoding_fixed2.json', 'w'))

def uniq(lyst):
    newlyst = []
    for item in lyst:
        if item not in newlyst:
            newlyst.append(item)
    return newlyst

main()
