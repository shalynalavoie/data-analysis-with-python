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

for row in exampleData[1:]:
    if row[2] not in candidates:
        candidates.append(row[2])

print(f"List of Candidates with votes: {candidates}")


#total number of votes each candidate won
candidate_votes = {}

for candidate in candidates:
    candidate_votes[candidate] = 0

for row in exampleData[1:]:
    candidate_votes[row[2]] += 1


#percentage of votes each candidate won

win_percent = {}
for candidate in candidate_votes:
    win_percent[candidate] = round(candidate_votes[candidate] / number_of_votes * 100)

for candidate in win_percent:
    print(f"Candidate {candidate} won {win_percent[candidate]} of the votes.")


#winner of election based on popular vote
most_votes = 0
winner = ''
for candidate in candidate_votes:
    if candidate_votes[candidate] > most_votes:
        most_votes = candidate_votes[candidate]
        winner = candidate
     

#Print Results of Election
print("Election Results")
print(number_of_votes)
print(win_percent)
print(f"The winner of the election is {winner}")

#Output text file
output_file = os.path.join("pypoll_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write("Election Results" + "\n")
    datafile.write(str(number_of_votes) + "\n")
    datafile.write(str(win_percent) + "\n")
    datafile.write(f"The winner of the election is {winner} \n")
    datafile.write("End of Report")
