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
            
                        
            base_salary = format(float(row[3]), ",.2f")
            bonus = format(float(float(row[3]) * float(row[4])), ",.2f")
            total_salary = format((float(row[3]) * float(row[4])) + float(row[3]), ",.2f")

            print(f'Base Salary: ${base_salary}')
            print(f'Bonus: ${bonus}')
            print(f'Total Salary: ${total_salary}')
            
            decision = input("Press 'q' to quit or any other key to see the next employee's details: ")

            if decision == 'q':
                break
            print('')

main()


