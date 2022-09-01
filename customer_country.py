import csv
from csv import *

def main():
    infile = open('customers.csv', 'r')
    csvfile = csv.reader(infile)
    next(csvfile)

    outfile = open('customer_country.csv', 'w', newline="")
    csvwriter = csv.writer(outfile)

    headers = ["Full Name", "Country"]
    csvwriter.writerow(headers)

    count = 0
    for row in csvfile:
        csvwriter.writerow([row[1] + " " + row[2], row[4]])
        count += 1

    print(count)

main()

