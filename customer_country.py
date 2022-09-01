import csv

def main():
    infile = open('customers.csv', 'r')
    csvfile = csv.reader(infile)

    for row in csvfile:
        print(row)

main()

