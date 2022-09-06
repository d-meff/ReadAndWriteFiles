import csv
from csv import *

def main():
    infile = open('employeepay.csv', 'r')
    csvfile = csv.reader(infile)
    next(csvfile)

    decision = 'y'

    while decision != 'q':
        for row in csvfile:
            print(f'Full Name: {row[1]} {row[2]}')

            # didn't format these as currency but it wasn't specified in the instructions
            print(f'Base Salary: {row[3]}')
            print(f'Bonus: {round(float(row[3]) * float(row[4]), 2)}')
            print(f'Total Comp: {round(float(row[3]) * float(row[4]), 2) + float(row[3])}')
            
            decision = input("Press 'q' to quit or any other key to see the next employee's details: ")

            if decision == 'q':
                break
            print('')

main()


