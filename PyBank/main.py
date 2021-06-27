#Modules
import os
import csv
import datetime

#Set paths for files
csv_budget = os.path.join('./Resources/budget_data.csv')
#csv_election = os.path.join('./Resources/election_data.csv')

#Open the CSVs
#budget_file=open(csv_budget)
with open(csv_budget) as budget_data:
    
    budget_reader = csv.reader(budget_data)
    headings = next(budget_reader)
    old_row = next(budget_reader)

    total_months = 1
    net = 0
    avg_chg = 0

    changes = []

    print(old_row)
    
    for row in budget_reader:
        total_months += 1
        net += int(row[0])

       # print('each row', row)
        avg_chg = int(row[1]) - int(old_row[1])
        changes += [avg_chg]

        old_row = row
             
 
    changes_grand_total = sum(changes) / len(changes)
    answer = str(round(changes_grand_total, 2))
    print('Changes avg $', answer)
    print('Total months:', total_months)
    print('Total: $',net)


    final_answer = (
        f"Analysis \n"
        f"Total Months: {total_months}\n"
        f"Total: ${net}\n"
        f"Changes avg: ${answer}\n"
    )

    print(final_answer)
    
    output_path=os.path.join('./analysis/analysis.txt')
    with open(output_path, 'w') as txtfile:
        txtfile.write(final_answer)



# print("Budget!!! : ",budget_reader)



# print("all the rows!!!! : ",budget_reader)

# list_of_budget_columns =[]
# for row in everything:
#     #list_of_budget_columns.append(row)
#     print("Each row!!  :", row)
   
   
   
#     break
#print("The headings in budget_data.csv are : ", list_of_budget_columns[0])

# total_months = 0
# total_net = 0
# first_row = next(reader)
# total_months += 1
# total_net += int(first_row[1])
# prev_net = int(first_row[1])

# for row in budget_reader:
#     total_months +=1
#     total_net += int(row[1])
# print("Total Months: ", total_net)    

#election_file=open(csv_election)
# election_reader = csv.reader(election_file, delimiter=',')
# list_of_election_columns =[]
# for row in election_reader:
#     list_of_election_columns.append(row)
#     break
# print("The headings in election_data.csv are : ", list_of_election_columns[0]),


#Variables for PyBank
#months_count =[],
#months_count['MonthSort']=months_count[list_of_budget_columns].apply(lambda x: x.month),
# total_months = []
# total_net = []
# for row in list_of_budget_columns:
    
#     break
# print("Total Months:", total_net)

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

