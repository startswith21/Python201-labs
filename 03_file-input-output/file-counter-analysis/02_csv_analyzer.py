# Use the `csv` module to read in and count the different file types.
import pathlib
import csv

with open ("filecounts.csv", "r") as csvfile:
    reading = csv.DictReader(csvfile, fieldnames = ["doc", "exc", "png", "pdf"])
    counting = list(reading)
    print(counting)

for dict in counting:        #listing key & values of both dicts in list
    for key in dict:
        print(key, dict[key])

for key in counting[0].values():  #accessing values of selected dictionary
    print(key)

for key, value in counting[1].items():  #accessing key and value of selected dictionary
    print(key, value)
