import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources","election_data.csv")

total_votes = 0
total_votes_list = []
candidates_dic = {}
per_votes = 0
winner = " "
candidate = " "

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)
    
    
    for row in csvreader:
        total_votes = total_votes + 1 
        total_votes_list.append(row[0])

        candidate = (row[2])
        
        if candidate in candidates_dic:
            candidates_dic[candidate] = candidates_dic[candidate] + 1
            
        else:
            candidates_dic[candidate] = 1 
    




            
        
    
        






print("Election Results")
print("---------------------------")
print(f"Total Votes: {str(total_votes)}")
print("----------------------------")
for candidate in candidates_dic.items():
    print(f"{candidate}: ")
print("-----------------------------")    
for candidate in candidates_dic.keys():
    if candidates_dic[candidate] > per_votes:
        winner = candidate
        per_votes = candidates_dic[candidate]
        print(f" Winner: {candidate} ")

