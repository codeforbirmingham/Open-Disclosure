#!/usr/bin/python3

# reads in "2014_Geocoding.json" and rounds all coordinates to
# 6 decimals, which gives a precision of about 0.1m

import json

def main():
    f = open('../data/2014_Geocoding.json')
    j = json.load(f)
    newJ = {}
    for key in j.keys():
        temp = j[key]
        if len(temp['coords']) > 0:
            temp['coords'] = {'lat': round(j[key]['coords']['lat'], 6),
                              'lng': round(j[key]['coords']['lng'], 6)}
        newJ[key] = temp
    json.dump(newJ, open('../data/2014_Geocoding_fixed.json', 'w'))

main()
