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



        
