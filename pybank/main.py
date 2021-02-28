#import my dependancies
import os
import csv

total_months = 0
net_total = 0
monthly_change = []
monthly_count  = []
greatest_increase = 0
greatest_decrease = 0
monthly_increase = 0
monthly_decrease = 0



#create file path
budget_data_path = os.path.join("../pybank/resources/budget_data.csv")


#open and read data path
with open(budget_data_path) as budget_data_file:
    reader = csv.reader(budget_data_file , delimiiter=',')

    #read the header row first
    header = next(reader)
    row = next(reader)

    #determine how many total_months
    previous_rows = int(row[1])
    total_months = total_months + 1

    #determine the total revenue
    net_total = net_total + int(row[1])

    #determine greatest increase
    greatest_increase = int(row [1])
    monthly_increase = row[0]

    #read eaach row after headers
    for row in reader:

        #determine total number of months in dataset
        total_months = total_months + 1

        # determine net total profit/loss for whole period
        net_total = net_total + int(row[1])

        # determine the change for months
        revenue_change = int(row [1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row [1])
        monthly_count.append(row[0])

        #calculate the greatest monthly_decrease
        if int(row[1] < greatest_increase:
            greatest_increase = int(row[1])
            monthly_decrease = row [0]

    #determine the mean and the date
    average_changes = sum(monthly_change) / len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

#print statements
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Amount: ${net_total}")
print(f"Average Change: ${average_changes}")
print(f"Greatest Incrase in Profits:,{monthly_increase}, (${highest})")
print(f"Greatest Decrease in Profits:, {monthly_decrease},${lowest})")

# write edited data to file
output_file = os.path.join("../pybank/analysis/budget_data_reviewed.txt")

#open file as text file
with open(output_file, 'w',) as txtfile:

    #format
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total Amount: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_changes}\n")
    txtfile.write(f"Greatest Incrase in Profits:,{monthly_increase}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {monthly_decrease},${lowest})\n")
    
