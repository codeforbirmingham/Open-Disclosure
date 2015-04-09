import json

def main():
    f = open("../data/2014_Geocoding.json")
    j = json.load(f)
    print(len(j.keys()))
    input()
    for key in j.keys():
        print(j[key])
        input()

main()
