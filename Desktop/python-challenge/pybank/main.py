#create file path
import os
import csv

csv_file = os.path.join('..', 'Pybank', 'Resources', 'budget_data.csv')

exampleFile = open('./Resources/budget_data.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

number_of_months = []
for row in exampleData[1:]:
    if row[0] not in number_of_months:
        number_of_months.append(month[0])

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

#greatest increase in profits date/amount over entire period
greastestinc = profit_loss_list[0]
greatestdec = profit_loss_list[0]

for i in range(len(profit_loss_list)):
    if profit_loss_list[i] >= greastestinc:
        greatestinc = profit_loss_list[i]
        greatestincmonth = date[i]

#greatest decrease in losses date/amount over entire period
    elif profit_loss_list[i] <= greatestdec:
        greatestdec = profit_loss_list[i]
        greatestdecmonth = date[i]
