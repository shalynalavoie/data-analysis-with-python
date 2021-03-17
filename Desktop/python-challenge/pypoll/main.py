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

#percentage of votes each candidate won

#total number of votes each candidate won

#winner of election based on popular vote
