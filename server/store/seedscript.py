import csv

# data = list()
# with open('sample-data.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         data.append(row)

# print(data)



#def addusers():


def data():
    data = list()
    with open('sample-data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data   
 