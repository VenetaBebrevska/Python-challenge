# This is main.py in PyBank
# Import modules
import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Read CSV
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies deimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
   
    # Read each row of data after the header
    for row in csvreader:
        print(row)

# The total number of months included in the dataset (minus 1 for the header)
with open(csvpath) as csvfile:
    month_count = sum(1 for month in csvfile)-1
    print(month_count if month_count else 'Empty')

# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
#def average(X)
    #length = len(X)
    #total = 0.0
    #for profit in X:
        #total += profit
    #return total / length

    #print(average(X))    

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period





        
