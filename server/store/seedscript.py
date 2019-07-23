import csv
import os

def processrow(row):
        result = []
        result.append(row[0])
        index = row[1].find('-')
        item = row[1][0: index]
        result.append(item)
        idxDetails = row[1].find('Details:')
        idxFabric = row[1].find('Fabric:')
        idxWeight = row[1].find('Weight:')
        details = row[1][idxDetails:idxFabric]
        fabric = row[1][idxFabric:idxWeight]
        weight = row[1][idxWeight:]
        result.append(fabric)
        result.append(weight)
        return result

def data():
    data = list()
    cwd = os.getcwd()  # Get the current working directory (cwd)
    with open(cwd + '/store/sample-data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
           #print("blah:",row,"/n")
           row = processrow(row)
           data.append(row)
    return data   
 