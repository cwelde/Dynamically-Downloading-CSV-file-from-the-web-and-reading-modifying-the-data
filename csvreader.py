import csv
import math

with open('angles_UCI_CS.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')

    stationIDs = {}

    for row in readCSV:
        stationIDs[row[0]] = row[1]


del stationIDs['station_id']

adict = {k:math.cos(float(v)) for k, v in stationIDs.items()}

print("The format is a dictionary where the key is a Station ID as a string, and the value is the cosine of the angle as float")
print(adict)


        
