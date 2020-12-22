import os
import csv

#Path to collect data from the Bank Resources folder
pybank_csv = os.path.join("Resources", "budget_data.csv")

#Open the CSV
with open(pybank_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#Define the columns and rows
pybank_csv = []
Date = row[0]
Profit/Losses = row[1]

for row in pybank_csv:
    if row[0] == Date:
        print(row[0] + "Just Dates")

#Find the total number of months in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period



minVal, maxVal = [], []
    for i in data:
        minVal.append(i[1])
        maxVal.append(i[2])

print min(minVal)
print max(maxVal)

#The greatest decrease in losses (date and amount) over the entire period

#Write this data to a new text file
