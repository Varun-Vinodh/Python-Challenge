
# To  import OS module in order to create file paths across operating systems
import os
# To import module for reading CSV files
import csv
import statistics

# To import cvs file
csvpath = os.path.join('/Users/varunvinodh/Downloads/Instructions 2/PyBank/Resources/budget_data.csv')

# Creating variables and lists to assign values later
total_months = 0
profitlosslist = []
datelist = []
monthlychangelist = []
avgchange = 0
monthlychange = 0
prevmonth = 0
totalchange = 0
biggestchange = 0
smallestchange = 0

# To read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        #print(row)
        profitandloss = int(row[1])
        date = str(row[0])

        # To calculate total months
        total_months = total_months + 1

        # To create a list with all profit/losses
        profitlosslist.append(profitandloss)

        # To ignore first change as there no preceding value
        if prevmonth == 0:
            prevmonth = int(row[1])
        else: 
            monthlychange = int(row[1]) - prevmonth
            prevmonth = int(row[1])
            totalchange = monthlychange + totalchange
            monthlychangelist.append(monthlychange)

    # To calculate average change, greatest increase and greatest decrease
    biggestchange = max(monthlychangelist)
    smallestchange = min(monthlychangelist)
    avgchange = totalchange/(total_months-1)
    avrgchange = round(avgchange,2)

    
# To open to text file to export analysis
file = open('pybank.txt', 'w')

# To print required information and export analysis to text file

print("Financial Analysis")
file.write("Financial Analysis")
print("------------------------------")
file.write('\n'"------------------------------")

total = (total_months)

print(f"Total Months: {total}")
file.write('\n'f"Total Months: {total}")

rev = sum(profitlosslist)
print(f"Total: ${rev}")
file.write('\n'f"Total: ${rev}")

print(f"Average change: ${avrgchange}")
file.write('\n'f"Average change: ${avrgchange}")
print(f"Greatest Increase in profits: (${biggestchange})")
file.write('\n'f"Greatest Increase in profits: (${biggestchange})")
print(f"Greatest Decrease in profits: (${smallestchange})")
file.write('\n'f"Greatest Decrease in profits: (${smallestchange})")


file.close()