#Modules
import os
import csv
import datetime

#Set paths for files
csv_budget = os.path.join('budget_data.csv')
csv_election = os.path.join('election_data.csv')

#Open the CSVs
budget_file=open(csv_budget)
budget_reader = csv.reader(budget_file, delimiter=',')
list_of_budget_columns =[]
for row in budget_reader:
    list_of_budget_columns.append(row)
    break
print("The headings in budget_data.csv are : ", list_of_budget_columns[0])

total_months = 0
total_net = 0
first_row = next(reader)
total_months += 1
total_net += int(first_row[1])
prev_net = int(first_row[1])

for row in budget_reader:
    total_months +=1
    total_net += int(row[1])
print("Total Months: ", total_net)    

election_file=open(csv_election)
election_reader = csv.reader(election_file, delimiter=',')
list_of_election_columns =[]
for row in election_reader:
    list_of_election_columns.append(row)
    break
print("The headings in election_data.csv are : ", list_of_election_columns[0]),


#Variables for PyBank
#months_count =[],
#months_count['MonthSort']=months_count[list_of_budget_columns].apply(lambda x: x.month),
total_months = []
total_net = []
for row in list_of_budget_columns:
    
    break
print("Total Months:", total_net)

# for month in list_of_budget_columns[0:]:
#     month_count = month[0]
#     month_total += month_count
#     break

#months_count = list_of_budget_columns.count[]
profit_change =[]
avg_change =[]
profit_high=[]
high_date = []
loss_high = []
loss_date = []

