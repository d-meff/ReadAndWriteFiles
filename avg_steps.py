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
            total_steps[2] += int(row[1])
            month_counts[2] += 1
        elif row[0] == '4':
            total_steps[3] += int(row[1])
            month_counts[3] += 1
        elif row[0] == '5':
            total_steps[4] += int(row[1])
            month_counts[4] += 1
        elif row[0] == '6':
            total_steps[5] += int(row[1])
            month_counts[5] += 1
        elif row[0] == '7':
            total_steps[6] += int(row[1])
            month_counts[6] += 1
        elif row[0] == '8':
            total_steps[7] += int(row[1])
            month_counts[7] += 1
        elif row[0] == '9':
            total_steps[8] += int(row[1])
            month_counts[8] += 1
        elif row[0] == '10':
            total_steps[9] += int(row[1])
            month_counts[9] += 1
        elif row[0] == '11':
            total_steps[10] += int(row[1])
            month_counts[10] += 1
        elif row[0] == '12':
            total_steps[11] += int(row[1])
            month_counts[11] += 1


    print(total_steps)
    print(month_counts)

main()