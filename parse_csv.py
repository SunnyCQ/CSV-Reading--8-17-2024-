import csv

#boilerplate code to open the csv. 'r' represents read
with open('TestCSVEng.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for hi in csv_reader:
        print(hi)