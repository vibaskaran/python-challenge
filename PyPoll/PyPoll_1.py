import os
import csv
from itertools import groupby
from operator import itemgetter

csvpath = os.path.join("raw_data", "election_data_1.csv")
output_path = os.path.join('output', 'election_data_1_output.csv')
csv_dict_list = []
Total_Voters = 0
csv_dict = {}
count = 0

csv_reader = csv.DictReader(open(csvpath))
   
for row in csv_reader:
    for column, value in row.items():
        csv_dict.setdefault(column, []).append(value)

Total_Voters = len(csv_dict['Voter ID'])
County_list = list(set(csv_dict['County']))
Candidate_list = list(set(csv_dict['Candidate']))
print (Total_Voters)
print (County_list)
print (Candidate_list) 

for Candidate in Candidate_list:
    for value in csv_dict:
        #print(sum(csv_dict.get('Candidate')))
        if csv_dict.get('Candidate') == Candidate:
            count += 1
        print(count)  

