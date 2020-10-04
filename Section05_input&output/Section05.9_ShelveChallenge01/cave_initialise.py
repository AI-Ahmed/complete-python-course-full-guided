__author__ = "crypto"

import shelve

locations = shelve.open("map")
locations['0'] = {"des": "You're sitting in front of a computer learning python",
                  "exits": {},
                  "namedExits": {}}

locations['1'] = {"des": "You're standing at the end of a road before a small brick building",
                  "exits": {"W": '2', "E": '3', "N": '5', "S": '4'},
                  "namedExits": {"2": '2', "3": '3', "4": '4', "5": '5'}}

locations['2'] = {"des": "You're at the top of a hill",
                  "exits": {"N": '5', "Q": '0'},
                  "namedExits": {"5": '5'}}

locations['3'] = {"des": "You're inside a building, a well house for a small stream",
                  "exits": {"W": '1', "Q": '0'},
                  "namedExits": {"1": '1'}}

locations['4'] = {"des": "You're in a valley beside a stream",
                  "exits": {"W": '2', "N": '1', "Q": '0'},
                  "namedExits": {"1": '1', "2": '2'}}

locations['5'] = {"des": "You're in the forest",
                  "exits": {"Q": '0', "S": '1', "W": '2'},
                  "namedExits": {"1": '1', "2": '2'}}

locations.close()

letters = shelve.open("vocabulary")

letters["QUIT"] = "Q"
letters["WEST"] = "W"
letters["EAST"] = "E"
letters["NORTH"] = "N"
letters["SOUTH"] = "S"
letters["ROAD"] = "1"
letters["HILL"] = "2"
letters["BUILDING"] = "3"
letters["VALLEY"] = "4"
letters["FOREST"] = "5"

letters.close()
