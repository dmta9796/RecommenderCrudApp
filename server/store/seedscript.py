import csv
import os
import re
from . import models

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
        fabric = row[1][idxFabric:idxWeight] #.split('.')[0:2]
        #strfabric = fabric[0]+'.'+fabric[1]
        #print(fabric)
        weight = row[1][idxWeight:]
        result.append(fabric)
        result.append(weight)
        return result

def processdata(data):
        result = []
        result.append(data[0]) # id number of item
        info = data[1].split('<br><br>')
        #print(info,len(info))
        info[0] = info[0].split('-')[0]
        info[1] = info[1].split('</li>')
        info[2] = info[2].split(':')
        if(len(info) == 5):
                info[3] = info[3].split('</b>')[1]
        del info[1]
        print(info,len(info))

        return info

def data():
        data = list()
        cwd = os.getcwd()  # Get the current working directory (cwd)
        with open(cwd + '/store/sample-data.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                        row = processdata(row)
                        #row = processrow(row)
                        data.append(row)
        return data   
 