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
candidate = str(exampleData[3:])
list_candidateswithvotes = len(exampleData[3:])
#print(f"List of Candidates with votes: {candidate}")

#percentage of votes each candidate won
number_of_votes = [int(row[3] for row in exampleData
win_percent = (candidate / number_of_votes) * 100


#total number of votes each candidate won

#winner of election based on popular vote
