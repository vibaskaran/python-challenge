import os
import csv
import locale


csvpath = os.path.join("raw_data", "budget_data_2.csv")

output_path = os.path.join('output', 'budget_data_2_output.csv')
locale.setlocale( locale.LC_ALL, '' )
csv_dict_with_strs = {}
csv_dict_with_ints = {}
Total_Months = 0
Total_Revenue = 0
Average_Revenue = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    csv_dict_with_strs = dict(csvreader)

csv_dict_with_ints = dict((k,int(v)) for k,v in csv_dict_with_strs.items()) # Converting the Value column as integer


Total_Revenue = sum(csv_dict_with_ints.values()) # getting total or all the values to find out total Revenue

Average_Revenue = Total_Revenue / Total_Months # getting Average Revenue

min_value = min(csv_dict_with_ints.values())  # minimum value
min_key = [k for k, v in csv_dict_with_ints.items() if v == min_value] # getting all keys containing the `minimum`

max_value = max(csv_dict_with_ints.values())  # maximum value
max_key = [k for k, v in csv_dict_with_ints.items() if v == max_value] # getting all keys containing the `maximum`

print()
with open(output_path, 'w', newline='') as csvfile:
    
    print('Financial Analysis')
    csvfile.writelines(['Financial Analysis'+ '\n'])

    print('----------------------------')
    csvfile.writelines(['----------------------------'+ '\n'])


    print('Total Months: ', Total_Months )
    csvfile.writelines('Total Months:  ' + str(len(csv_dict_with_ints.keys())) + '\n')

    print('Total Revenue: ',locale.currency(Total_Revenue,grouping = True))
    #csvfile.writelines(['Total Revenue: ',locale.currency(Total_Revenue,grouping = True)+ '\n'])

Total_Months = len(csv_dict_with_ints.keys()) # getting total no of keys to find out total months 
    print('Average Revenue Change: ',locale.currency(Average_Revenue,grouping = True))
    #csvfile.writelines(['Average Revenue Change: ',locale.currency(Average_Revenue,grouping = True)+ '\n'])

    print('Greatest Increase in Revenue: ',max_key,locale.currency(max_value,grouping = True) )
    #csvfile.writelines(['Greatest Increase in Revenue: ',max_key,locale.currency(max_value,grouping = True)+'\n'])

    print('Greatest Decrease in Revenue: ',min_key,locale.currency(min_value,grouping = True) )
    #csvfile.writelines(['Greatest Decrease in Revenue: ',min_key,locale.currency(min_value,grouping = True)])
print()