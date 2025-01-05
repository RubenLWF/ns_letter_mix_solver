import json
import re


def count_chars(s):
    string = re.sub(r'\W+', '', s).lower()

    char_dict = {}
    for c in string:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict


target = count_chars(input("Enter the station name: "))

data = json.load(open('stations.json', 'r'))

res = "No match found... :("
for station in data['stations']:
    char_dict = count_chars(station)

    if char_dict == target:
        res = station
        break

print(res)
