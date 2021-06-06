import os
import csv

csvpath = os.path.join('budget_data.csv','election_data.csv')
print(csvpath)

csvfile=open(csvpath)

csvreader = csv.reader(csvfile, delimiter=',')

