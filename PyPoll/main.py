import os
import csv
import math
import collections
from collections import Counter

#Path to collect data from the Bank Resources folder
pypoll_csv = os.path.join("Resources", "election_data.csv")

#Lists to store data
voter_id = [0]
country = [1]
candidate = [2]
correy_votes = 0
tooley_votes = 0
li_votes = 0
khan_votes = 0

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

#Count toal votes    
for line in data:
    r = line.split(",")
    total_votes = total_votes + float(r[0])
print("Total Votes:", votecounter)




#Create list of candidates
myList = ["Khan", "Correy", "O'Tooley", "Li"]
print(myList)



#Open the CSV
with open(pypoll_csv, "r") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_reader)

    #define column two as candidate vote
    def pypoll_csv(candidates):
        candidate = str(candidates[2])

    for row in csv_reader:
        if candidate == 'Khan':
            khan_votes = khan_votes + 1
    for row in csv_reader:        
        if candidate == "Li":
            li_votes = li_votes + 1
    for row in csv_reader:        
        if candidate == "O'Tooley":
            tooley_votes = tooley_votes + 1
    for row in csv_reader:        
        if candidate == "Correy":
            correy_votes = correy_votes + 1        

    print ("Khan recieved: ", khan_votes, "votes")
    print ("Li recieved: ", li_votes, "votes")
    print ("O'Tooley recieved: ", tooley_votes, "votes")
    print ("Correy recieved: ", correy_votes, "votes")


#print ('Khan received votes: %s' % khan_votes['Khan'])
#print (khan_votes.most_common())



#khan_result = Counter(khan_votes)
#make a dictionary of candidates
#electionresults = {
    #'Khan': len(khan_votes),
    #'Correy': len(correy_votes),
    #"O'Tooley": len(tooley_votes),
    #'Li': len(li_votes)}
#decide winner
#winner = (max(electionresults))

#print(len(khan_votes))




#average = float(total_votes / votecounter)
#print("The average change is: ", "%.2f" % average)



    
# Specify the file to write to
output_path = os.path.join("Output", "PyPoll_new.csv")
# Preview Output
PyPoll_new = os.path.join("Output", "PyPoll_new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(PyPoll_new, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csv_writer = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csv_writer.writerow(['Election Results'])

    # Write the second row
    csv_writer.writerow(['-----------------------------'])

    # And so on:
    csv_writer.writerow(['Total Votes:', votecounter])
    csv_writer.writerow(['-----------------------------'])
    csv_writer.writerow(['Khan:', khan_votes])
    csv_writer.writerow(['Correy:', correy_votes])
    csv_writer.writerow(['Li:', li_votes])
    csv_writer.writerow(['OTooley:', tooley_votes])
    csv_writer.writerow(['-----------------------------'])
    csv_writer.writerow(['Winner:', 'XX'])


