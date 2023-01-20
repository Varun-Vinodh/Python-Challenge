# To  import OS module in order to create file paths across operating systems
import os
# To import module for reading CSV files
import csv

# To import cvs file
csvpath = os.path.join('/Users/varunvinodh/Downloads/Instructions 2/PyPoll/Resources/election_data.csv')

total_ballots = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0 

# To read csv file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        #print(row)
        # To calculate total number of votes
        total_ballots += 1
        # To calculate total number of votes for Charles
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        # To calculate total number of votes for Diana
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        # To calculate total number of votes for Raymon
        elif row [2] == "Raymon Anthony Doane":
            raymon_votes += 1

# To calculate percentage of votes for each candidate and rounding to 3 decimal points
charles_votes_pr = ((charles_votes/total_ballots)*100)
charles_votes_prd = round(charles_votes_pr,3)
diana_votes_pr = ((diana_votes/total_ballots)*100)
diana_votes_prd = round(diana_votes_pr,3)
raymon_votes_pr = ((raymon_votes/total_ballots)*100)
raymon_votes_prd = round(raymon_votes_pr,3)

# To open to text file to export analysis
file = open('/Users/varunvinodh/Desktop/Python-Challenge/pypoll.txt', 'w')

# To print required information and export to text file
print("Election Results")
file.write("Election Results")
print("-------------------------------------")
file.write('\n'"-------------------------------------")
print(f"Total votes: {total_ballots}")
file.write('\n'f"Total votes: {total_ballots}")
print("-------------------------------------")
file.write('\n'"-------------------------------------")
print(f"Charles Casper Stockham: {charles_votes_prd}%  ({charles_votes})")
file.write('\n'f"Charles Casper Stockham: {charles_votes_prd}%  ({charles_votes})")
print(f"Diana DeGette: {diana_votes_prd}%  ({diana_votes})")
file.write('\n'f"Diana DeGette: {diana_votes_prd}%  ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_votes_prd}%  ({raymon_votes})")
file.write('\n'f"Raymon Anthony Doane: {raymon_votes_prd}%  ({raymon_votes})")
print("---------------------------------------")
file.write('\n'"---------------------------------------")
# To print winner based on who has highest amount of votes
if charles_votes>diana_votes and charles_votes>raymon_votes:
    print("Winner: Charles Casper Stockham")
    file.write('\n'"Winner: Charles Casper Stockham")
elif diana_votes>charles_votes and diana_votes>raymon_votes:
    print("Winner: Diana DeGette")
    file.write('\n'"Winner: Diana DeGette")
elif raymon_votes>charles_votes and raymon_votes>diana_votes:
    print("Winner: Raymon Anthony Doane")
    file.write('\n'"Winner: Raymon Anthony Doane")
print("---------------------------------------")
file.write'\n'("---------------------------------------")

file.close()