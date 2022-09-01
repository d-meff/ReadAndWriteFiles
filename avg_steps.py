from calendar import month
import csv

def main():
    infile = open('steps.csv', 'r')
    csvfile = csv.reader(infile, delimiter=',')


    total_steps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    month_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for row in csvfile:
        if row[0] == '1':
            total_steps[0] += int(row[1])
            month_counts[0] += 1
        elif row[0] == '2':
            total_steps[1] += int(row[1])
            month_counts[1] += 1
        elif row[0] == '3':
            total_steps[0] += int(row[1])
            month_counts[0] += 1
        elif row[0] == '4':
            total_steps[1] += int(row[1])
            month_counts[1] += 1
        elif row[0] == '5':
            total_steps[0] += int(row[1])
            month_counts[0] += 1
        elif row[0] == '6':
            total_steps[1] += int(row[1])
            month_counts[1] += 1
        elif row[0] == '7':
            total_steps[0] += int(row[1])
            month_counts[0] += 1
        elif row[0] == '8':
            total_steps[1] += int(row[1])
            month_counts[1] += 1
        elif row[0] == '9':
            total_steps[0] += int(row[1])
            month_counts[0] += 1
        elif row[0] == '10':
            total_steps[1] += int(row[1])
            month_counts[1] += 1
        elif row[0] == '11':
            total_steps[0] += int(row[1])
            month_counts[0] += 1
        elif row[0] == '12':
            total_steps[1] += int(row[1])
            month_counts[1] += 1


    print(total_steps)
    print(month_counts)

main()