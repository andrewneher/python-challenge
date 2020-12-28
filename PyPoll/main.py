import os
import csv
import math

#Path to collect data from the Bank Resources folder
pypoll_csv = os.path.join("Resources", "election_data.csv")

#Open the CSV
with open(pypoll_csv, "r") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")
    #print(csv_reader)

    # Read the header row first 
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

        # Read each row of data after the header
    #for row in csv_reader:
        #print(row[1])


#Create a bucket for Total Votes
poll = open(pypoll_csv, "r")
data = poll.readline()
print(poll)
data = poll.readlines()
total_votes = 0
votecounter = 0
for poll in data:
    votecounter = votecounter + 1
    

for line in data:
    r = line.split(",")
    total_votes = total_votes + float(r[0])
print("Total Votes:", votecounter)
#average = float(total_votes / votecounter)
#print("The average change is: ", "%.2f" % average)

#max_change = 0
#for line in data:
#    r = line.split(",")
#    max_change = max_change + float(r[1])
#    if max_change <= max_change:
#        break
#print("Maximum change is:", max_change)




#for line in data:
#    r = line.split(",")
#    value = float(r[2])
#    Khan = Khan + value




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
output_path = os.path.join("Output", "PyPoll_new.csv")
# Preview Output
PyBank_new = os.path.join("Output", "PyPoll_new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csv_writer = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csv_writer.writerow(['Election Results'])

    # Write the second row
    csv_writer.writerow(['-----------------------------'])

    # And so on:
    csv_writer.writerow(['Total Votes:', votecounter])
    csv_writer.writerow(['-----------------------------'])
    csv_writer.writerow(['Khan:', 'XX'])
    csv_writer.writerow(['Correy:', 'XX'])
    csv_writer.writerow(['Li:', 'XX'])
    csv_writer.writerow(['OTooley:', 'XX'])
    csv_writer.writerow(['-----------------------------'])
    csv_writer.writerow(['Winner:', 'XX'])

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
