import csv

with open('profiles.csv') as file:
    csv_reader = csv.reader(file)

    for line in csv_reader:
        print(line[0])
