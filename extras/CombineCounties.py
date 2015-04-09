# CombineCounties.py

import json
import os

def main():
    allCounties = {}
    for filename in os.listdir('../data/map/AL/'):
        thisCounty = {}
        with open('../data/map/AL/' + filename) as currentfile:
           thisCounty = json.load(currentfile)
           if len(allCounties) == 0:
               allCounties = thisCounty
           else:
               (allCounties['features']).append(thisCounty['features'][0])
    with open('../data/map/AL_Counties.geo.json', 'w') as outfile:
        json.dump(allCounties, outfile)

main()
