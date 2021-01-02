import os
import csv
import math
import collections
from collections import Counter


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

#Create list of candidates
myList = ["Khan", 0, "Correy", 0, "O'Toohley", 0, "Li", 0]
print(myList)


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


#count Khan candidate votes
#khan_votes = collections.Counter()
#for row in csv.reader(csvfile, delimiter=','):
#    khan_votes[row[2]] += 1

#print ('Khan received votes: %s' % khan_votes['Khan'])
#print (khan_votes.most_common())


khan_votes = 0
correy_votes = 0
tooley_votes = 0
li_votes = 0
#khan_result = Counter(khan_votes)
#make a dictionary of candidates
electionresults = {
    "Khan": len(khan_votes),
    "Correy": len(correy_votes),
    "O'Tooley": len(tooley_votes),
    "Li": len(li_votes)}
#decide winner
winner = (max(electionresults))

print(len(khan_votes))




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

    
# Specify the file to write to
output_path = os.path.join("Output", "PyPoll_new.csv")
# Preview Output
PyPoll_new = os.path.join("Output", "PyPoll_new.csv")

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


