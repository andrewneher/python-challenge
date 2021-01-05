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

winner = str


#Outfut Path
output_path = os.path.join("Output", "PyPoll_new.txt")


#Open the CSV
with open(pypoll_csv, "r") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")


    # Read the header row first 
    csv_header = next(csv_reader)




#Create a bucket for Total Votes
poll = open(pypoll_csv, "r")
data = poll.readline()
print(poll)
data = poll.readlines()

votecounter = 0
for poll in data:
    votecounter = votecounter + 1

#Count toal votes    
for line in data:
    r = line.split(",")

#Print total votes, formatted
print("  ")
print("------------------------------------------")
print("           Total Votes: ", votecounter)
print("------------------------------------------")




#Open the CSV
with open(pypoll_csv, "r") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_reader)
    #Create empty dictionary
    candidate_votes = {}
    for row in csv_reader:
        candidate = row [2]
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] +=1
        else:
            candidate_votes[candidate] = 1

#Add total votes
total_votes = sum(candidate_votes.values())


#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w") as csvfile:

    #Create empty list
    voters_percentage = []
    for i in candidate_votes:
        voters_percentage = (float(candidate_votes[i]) / total_votes) * 100

        #round the percentage, add line breakers
        election_data = (f"{i} {round(voters_percentage,0)}%  -  {candidate_votes[i]}\n")

        print(election_data)

        csvfile.write(election_data)
     

    #aggregate the data and choose a winner
    for key in candidate_votes.keys():
        if candidate_votes[key] == max(candidate_votes.values()):
            winner = key
  
  #Export winners and total votes, Format data for output
    print(">>>>---------------------------------<<<<")
    print("   The Winner of the Election is:", winner)
    print(">>>>---------------------------------<<<<")
    csvfile.write(f"\n{'Winner: '}")
    csvfile.write(winner)

    csvfile.write(f"\n{'Total Votes: '}")
    csvfile.write(f"{round(votecounter,0)}\n")   



