#!/usr/bin/python3

# reads in '2014_Organizations.json' and changes the 'id' keys to '_id',
# and changes the type values to either 'Candidate' or 'Committee'

import json

def main():
    f = open('../data/2014_Organizations.json')
    j = json.load(f)
    newJ = []
    for group in j:
        newGroup = {}
        newGroup['_id'] = group['id']
        newGroup['name'] = group['name']
        if group['type'] == 'Political Action Committee':
            newGroup['type'] = 'PAC'
        elif group['type'] == 'Principal Campaign Committee':
            newGroup['type'] = 'Candidate'
        else:
            print('Error: Unkown group type: ' + str(group))
            break
        newJ.append(newGroup)
    json.dump(newJ, open('../data/2014_Organizations_fixed.json', 'w'))

main()
