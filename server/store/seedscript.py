import csv
import os
import re
from . import models

def processdata(data):
        result = []
        result.append(data[0]) # id number of item
        info = data[1].split('<br><br>')
        #print(info,len(info))
        info[0] = info[0].split('-')[0]
        info[1] = info[1].split('</li>')
        info[2] = info[2].split(':')
        del info[2][0]
        info[2][0] = info[2][0].replace('</b>','')
        if(len(info) == 5):
                info[3] = int(info[3].split('</b>')[1].split('g')[0].replace('(','')) #weight of product in grams
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
                        data.append(row)
        return data   
 