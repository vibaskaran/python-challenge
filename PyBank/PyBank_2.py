# Dependencies
import csv
import locale
locale.setlocale( locale.LC_ALL, '' )

# Files to Load
file_to_load = "raw_data/budget_data_2.csv"
file_to_output = "output/budget_analysis_2.txt"

# Variables to Track
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

revenue_changes = []

# Read Files
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])
        # print(row)

        # Keep track of changes
        revenue_change = int(row["Revenue"]) - prev_revenue
        # print(revenue_change)

        # Reset the value of prev_revenue to the row I completed my analysis
        prev_revenue = int(row["Revenue"])
        # print(prev_revenue)

        # Determine the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        # Add to the revenue_changes list
        revenue_changes.append(int(row["Revenue"]))

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)
    
    # Show Output
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + locale.currency(total_revenue,grouping = True))
    print("Average Revenue Change: " + locale.currency(revenue_avg,grouping = True))
    print("Greatest Increase: " + str(greatest_increase[0]) + '  ('+ locale.currency(greatest_increase[1],grouping = True)+')')
    print("Greatest Decrease: " + str(greatest_decrease[0])  + '  ('+ locale.currency(greatest_decrease[1],grouping = True)+')')
    

# # Generate Output Summary
# output = (
#     f"\nFinancial Analysis\n"
#     f"----------------------------\n"
#     f"Total Months: {total_months}\n"
#     f"Total Revenue: ${total_revenue}\n"
#     f"Average Revenue Change: ${revenue_avg}\n"
#     f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
#     f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
# print(output)

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    #locale.currency(Average_Revenue,grouping = True)
    txt_file.write("Total Revenue: " + locale.currency(total_revenue,grouping = True))
    txt_file.write("\n")
    txt_file.write("Average Revenue Change: " + locale.currency(revenue_avg,grouping = True))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + '  ('+ locale.currency(greatest_increase[1],grouping = True)+')')
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0])  + '  ('+ locale.currency(greatest_decrease[1],grouping = True)+')')
    txt_file.write("\n")
    