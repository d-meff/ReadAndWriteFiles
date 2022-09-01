import csv

def main():
    infile = open('customers.csv', 'r')
    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile) # skips first row

    record = []

    x = 'y'

    while x == 'y':
        for row in csvfile:
            print(row[0])
            print(row[1])
            x = input('Continue?')

            if x != 'y':
                break

main()


