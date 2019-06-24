import csv
import os


#def addusers():


def data():
    data = list()
    cwd = os.getcwd()  # Get the current working directory (cwd)
    with open(cwd + '/store/sample-data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data   
 