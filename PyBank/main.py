#I don't think I did this correctly, but at least it is running

import os
import csv
import math

#Path to collect data from the Bank Resources folder
pybank_csv = os.path.join("Resources", "budget_data.csv")

#Open the CSV
with open(pybank_csv, "r") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)



#Create buckets for amounts
bank = open(pybank_csv, "r")
data = bank.readline()
print(bank)
data = bank.readlines()
total_months = 0
linecounter = 0
max_change = 0
for bank in data:
    linecounter = linecounter + 1
    
print("The total number of months is:", linecounter)

for line in data:
    r = line.split(",")
    total_months = total_months + float(r[1])
print("The total amount is:", total_months)
average = float(total_months / linecounter)
print("The average change is: ", "%.2f" % average)



total = 0
max_value = 0
min_value = 0

#Finding Max and Minimum Values
for line in data:
    r = line.split(",")
    value = float(r[1])
    total = total + value
    max_value = max(max_value, value)
    min_value = min(min_value, value)
print("The maximum change is:",  max_value )
print("The minimum change is:",  min_value )


        
# Specify the file to write to
output_path = os.path.join("Output", "PyBank_new.csv")
# Preview Output
PyBank_new = os.path.join("Output", "PyBank_new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csv_writer = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csv_writer.writerow(['Financial Analysis'])

    # Write the second row
    csv_writer.writerow(['-----------------------------'])

    # And so on:
    csv_writer.writerow(['Total Months:', linecounter])
    csv_writer.writerow(['Total:', total_months])
    csv_writer.writerow(['Average Change:', average])
    csv_writer.writerow(['Greatest Increase in Profits:', max_value])
    csv_writer.writerow(['Greatest Decrease in Profits:', min_value])


