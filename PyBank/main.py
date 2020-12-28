import os
import csv
import math

#Path to collect data from the Bank Resources folder
pybank_csv = os.path.join("Resources", "budget_data.csv")

#Open the CSV
with open(pybank_csv, "r") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")
    print(csv_reader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

        # Read each row of data after the header
    for row in csv_reader:
        print(row[1])


#Create a bucket for Total Months

bank = open(pybank_csv, "r")
data = bank.readline()
print(bank)
data = bank.readlines()
total_months = 0
linecounter = 0
for bank in data:
    linecounter = linecounter + 1
    
print("The total number of months is", linecounter)

for line in data:
    r = line.split(",")
    total_months = total_months + float(r[1])
print("The total amount is", total_months)
average = float(total_months / linecounter)
print("The average change is ", "%.2f" % average)

#print(total_months)
#data['Profit/Losses'].average

#create a bucket for Total
#sumamount = math.fsum(row[1])
#print(int(sumamount))

#create a bucket for Average Change
#average_change = mean(total)

#create a bucket for Greatest Increase in Profits
#greatest_increase = 

#create a bucket for Greatest Increase in Profits
#greatest_decrease =
        
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
    csv_writer.writerow(['Greatest Increase in Profits:', 'Need this figure'])
    csv_writer.writerow(['Greatest Decrease in Profits:', 'Need this figure'])

print(PyBank_new)

#Define the columns and rows
#pybank_csv = []
#Date = row[0]
#Profit/Losses = row[1]

#for row in pybank_csv:
    #if row[0] == Date:
        #print(row[0] + "Just Dates")

#Find the total number of months in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period



#minVal, maxVal = [], []
    #for i in data:
        #minVal.append(i[1])
        #maxVal.append(i[2])

#print min(minVal)
#print max(maxVal)

#The greatest decrease in losses (date and amount) over the entire period

#Write this data to a new text file
