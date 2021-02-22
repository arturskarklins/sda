import csv

with open('profiles.csv', 'w') as file:
    # file.write('Bob,Anna')
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age'])
    csv_writer.writerow(['Anna', 34])
    csv_writer.writerow(['Bob', 48])
