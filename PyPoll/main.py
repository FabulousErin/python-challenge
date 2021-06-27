#Modules
import os
import csv
import datetime

#Set path for file
csv_election = os.path.join('./Resources/election_data.csv')

#Open the CSV
with open(csv_election) as election_data:
    election_reader = csv.reader(election_data)
    headings = next(election_reader)
    old_row = next(election_reader)

    total_votes = 1
    net = 0
    avg_chg = 0

    changes = []

    print(old_row)
    
    for row in election_reader:
        total_votes += 1
        net += int(row[1])

       # print('each row', row)
        # avg_chg = int(row[1]) - int(old_row[1])
        # changes += [avg_chg]

        # old_row = row
             
 
    # changes_grand_total = sum(changes) / len(changes)
    # answer = str(round(changes_grand_total, 2))
    # print('Changes avg $', answer)
    # print('Total months:', total_months)
    print('Total: $',net)


    final_answer = (
        # f"Analysis \n"
        # f"Total Months: {total_months}\n"
        f"Total: ${net}\n"
        # f"Changes avg: ${answer}\n"
    )

    print(final_answer)
    
    output_path=os.path.join('./analysis/analysis.txt')
    with open(output_path, 'w') as txtfile:
        txtfile.write(final_answer)
