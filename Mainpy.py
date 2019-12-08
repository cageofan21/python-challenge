import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources","election_data.csv")

total_votes = 0
candidates_votes = []
candidates_won =[]

with open(csvpath, newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    csvheader =next(csvreader)