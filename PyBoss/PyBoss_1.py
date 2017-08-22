import csv
import datetime as d
import os

csvpath = os.path.join("raw_data", "employee_data1.csv")
output_path = os.path.join('output', 'employee_data1_output.csv')
Emp_list = []
Name = []
SSN = []

First_Name_list = []
Last_Name_list = []
DOB_list = []
SSN_list = []
State_list = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'}

#csv_reader = csv.DictReader(open(csvpath))

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)

    for row in csv_reader:
        #print(row)
        Emp_list.append(row[0])
        Name = row[1].split(' ')
        First_Name_list.append(Name[0])
        Last_Name_list.append(Name[1])
        dob = d.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y')
        DOB_list.append(dob)
        SSN = row[3].split('-')
        New_SSN = '***-**-'+SSN[2]
        SSN_list.append(New_SSN)
        state = us_state_abbrev.get(row[4])
        State_list.append(state)

Collections = zip(Emp_list, First_Name_list, Last_Name_list,DOB_list,SSN_list,State_list)

with open(output_path, 'w', newline="") as csvFile:

        csvWriter = csv.writer(csvFile, delimiter=',')

        csvWriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

        csvWriter.writerows(Collections)    