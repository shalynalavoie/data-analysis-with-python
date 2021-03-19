#create file path
import os
import csv

csv_file = os.path.join('.', 'Resources', 'pypoll.csv')

exampleFile = open(csv_file)
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

#total number of votes cast

number_of_votes = len(exampleData[1:])
print('The total number of votes is: ')  
print(str(number_of_votes))


#complete list of candidates who received votes
candidates = []

for row in exampleData:
    #print(row[2])
    if row[2] not in candidates:
        candidates.append(row[2:])

print(f"List of Candidates with votes: {candidates}")


#total number of votes each candidate won
candidate_votes = {}
for candidate in candidates:
    candidate_votes[candidate] = 0

for row in exampleData:
    candidate_votes[row[2]] =+1
    print(candidate_votes[row[2]])


#percentage of votes each candidate won

win_percent = {}
for candidate in candidate_votes:
    win_percent[candidate] = (candidate_votes[candidate] / number_of_votes * 100)

for candidate in win_percent:
    print(f"Candidate {candidate} won {win_percent[candidate]} of the votes.")


#winner of election based on popular vote
winning_votes = {}
if candidate > candidate:
    print(f"The winner of the election is {candidate}")
    

#Print Results of Election
print("Election Results")
print(number_of_votes)
print(win_percent)
print("The winner of the election is {candidate}")

#Output text file
output_file = os.path.join("pypoll_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write("Election Results")
    datafile.write(number_of_votes)
    datafile.write(win_percent)
    datafile.write("The winner of the election is {candidate}")
    datafile.write("End of Report")
