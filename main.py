import csv
import os

FILE_DATA = "data-398-2018-08-30.csv"
PATH_FILE_TOKEN = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(PATH_FILE_TOKEN, FILE_DATA)


def data_bus_station():
    with open(full_path, 'r', encoding='UTF-8') as f:
        data = csv.DictReader(f)
        l = []
        for row in data:
            d = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            l.append(d)
    return l

s = data_bus_station()
for i in s:
    print(f"{i['Name']}/ {i['Street']}/ {i['District']}")


