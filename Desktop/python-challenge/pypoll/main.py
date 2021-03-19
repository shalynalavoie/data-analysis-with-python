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


#complete list of cadidates who received votes
candidates = []

for row in exampleData:
    print(row[2])
    if row[2] not in candidates:
        candidates.append(row[2:])

print(f"List of Candidates with votes: {candidates}")


#total number of votes each candidate won
candidate_votes = {}
for candidate in candidates:
    candidate_votes[candidate] = 0

for row in exampleData
    candidate_votes[row[2]] =+1
    print(candidate_votes[row2]) 


#percentage of votes each candidate won

win_percent = (candidate_votes / number_of_votes) * 100
print(win_percent)



#winner of election based on popular vote
winner = 
