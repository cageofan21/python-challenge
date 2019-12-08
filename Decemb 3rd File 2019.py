import os 
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources", "budget_data.csv")

month_count = 0
total_months = 0
total_months_list = []
total_net = 0 
total_net_list = []
average_changes = 0
greatest_increase = 0
greatest_decrease = 0
max = 0
min = 0
min_month = " "
max_month = " "

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:

    #total months
        total_months = total_months + 1 
        total_months_list.append(row[0])
    print(f"Total Months: {(total_months)}") 

    #total Profit/Losses
    total_net = total_net + int(row[1])
    total_net_list.append(row[1])
    print("Total:" + "$" + str(total_net))

    #Average of changes in "Profit/Losses over entire period"
    


    
    #Greatest Increase/Decrease in Profits/Losses over entire period
    if (int(row[1])> max):
        max = int(row[1]) 
        max_month = row[0]
    elif (int(row[1]) < min):
        min = int(row[1]) 
        min_month = row[0] 
    print(f"Greatest Increase in Profits: {max_month} (${str(max)})")
    print(f"Greatest Decrease in Profits: {min_month} (${str(min)})")