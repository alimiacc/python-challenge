#standard import csv modules
import os
import csv

#define csv file with file_name
file_name = 'election_data.csv'
#path the python code to look for the already defined csv file from above (file_name)
csvpath = os.path.join('Resources',file_name)

# Open the file in "read" mode ('r') 
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #set your variables
    votes = 0
    candidates = []
    votes_counts = []


    #pass over the header info 
    row = next(csvreader,None)

    #start the for loop to run through all rows int he csv
    for row in csvreader:
        
        #calculate sum of total votes
        votes = votes +1
        #candidate voted for
        candidate = row[2]
        #start the tally of how many votes each candidate got 
        #if candidate matches index then tally additional votes to thier total
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            votes_counts[candidate_index] = votes_counts[candidate_index] + 1
        #if new candidate make new entry for them in list
        else:
            candidates.append(candidate)
            votes_counts.append(1)

percentages = []
max_index = 0
max_votes = votes_counts[0]

#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = votes_counts[count]/votes*100
    percentages.append(vote_percentage)
    if votes_counts[count] > max_votes:
        max_votes = votes_counts[count]
        print(max_votes)
        max_index = count
#find winner
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {round(percentages[count])}% ({votes_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#name the file you will export
write_file = f"pypoll_voting_results.txt"

#open the file to begin to write to the file
filewriter = open(write_file, mode = 'w')

#write/print analysis to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {votes}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {round(percentages[count])}% ({votes_counts[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()