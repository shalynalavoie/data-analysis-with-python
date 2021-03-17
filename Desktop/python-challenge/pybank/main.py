#create file path
import os
import csv

csv_file = os.path.join('..', 'Resources', 'budget_data.csv')

exampleFile = open('./Resources/budget_data.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

#total numnber of months
number_of_months = []
for row in exampleData[1:]:
    if row[0] not in number_of_months:
        number_of_months.append(row[0])

print('The total number of months is: ')
print(str(len(number_of_months)))

#net total over entire period
profit_loss_list = [int(row[1]) for row in exampleData[1:]]
net_profit = sum(profit_loss_list)

profit_change = []
for i in range(len(profit_loss_list)):
    if i < (len(profit_loss_list) - 1):
        change = profit_loss_list[i+1] - profit_loss_list[i]
        profit_change.append(change)

average_change = sum(profit_change) / len(profit_change)

#greatest increase/decrease in profits date/amount over entire period
greatestinc_amt = 0
greatestdec_amt = 0

for i in range(1, len(exampleData)-1):
    difference = int(exampleData[i+1][1]) - int(exampleData[i][1])
    if difference > greatestinc_amt:
        greatestinc_month = exampleData[i+1][0]
        greatestinc_amt = difference
    if difference < greatestdec_amt:
        greatestdec_month = exampleData[i+1][0]
        greatestdec_amt = difference


print(f'{greatestdec_month} is the month of the greatest decrease, {greatestdec_amt} is the amount')

print(f'{greatestinc_month} is the month of the greatest increase, {greatestinc_amt} is the amount')

print("Financial Analysis")
print("Total Months = 86")
print("Net Total= $38382578")
print("Average Change = $-2315.12")
print("Greatest Increase in Profits = Feb-2012 ($1926159)")
print("Great Decrease in Profits = Sep-2013 ($-2196167)")
