import csv
from csv import *

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

    month_avg_steps = []

    for i in range(0, 12):
        month_avg_steps.append(round(total_steps[i] / month_counts[i],1))

    outfile = open('avg_steps.csv', 'w', newline="")
    csvwriter = csv.writer(outfile)

    headers = ["Month", "Average Steps"]
    csvwriter.writerow(headers)

    csvwriter.writerow(['January', month_avg_steps[0]])
    csvwriter.writerow(['February', month_avg_steps[1]])
    csvwriter.writerow(['March', month_avg_steps[2]])
    csvwriter.writerow(['April', month_avg_steps[3]])
    csvwriter.writerow(['May', month_avg_steps[4]])
    csvwriter.writerow(['June', month_avg_steps[5]])
    csvwriter.writerow(['July', month_avg_steps[6]])
    csvwriter.writerow(['August', month_avg_steps[7]])
    csvwriter.writerow(['September', month_avg_steps[8]])
    csvwriter.writerow(['October', month_avg_steps[9]])
    csvwriter.writerow(['November', month_avg_steps[10]])
    csvwriter.writerow(['December', month_avg_steps[11]])

main()