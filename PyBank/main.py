# Python Challenge No 1. using Real World Challenge
# Analyze the fianncial records of the company

# Importing dependencies
import os
import csv


# create a path to a file named "budget_data.csv"
output_path = os.path.join ('python_challenge\PyBank\Resources\BBudget_data.csv')

# declaring and initializing variables to be used in the script
Total_months = 0 # Variable for calcualtin total months
Total_net_profit_loss = 0 # Variable for net total amount of Profit/loss over the next period
prev_profit_loss = 0 # Variable for changes of Profit/loss over entire period
monthly_changes = [] # Variable for changes of Profit/loss monthly
Avg_changes_profit_loss = 0.0 # Variable for average of changes of Profit/loss over entire period
greatest_increase_in_profit = [" ", 0] # Variable for greatest increase for entire period
greatest_decrease_in_profit = [" ", 0] # Variable for greatest decrease for entire period

# reading csv file
with open (output_path, 'r' , newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skipping header row
    header = next(csvreader)

    # loop each row in csv
    for row in csvreader:
        # calculate total number of months
        Total_months +=1

        #calculate total profit losses
        Total_net_profit_loss += int(row[1])
            
        # Calculate monthly changes     
        if Total_months > 1:
            monthly_change = int(row[1]) - prev_profit_loss
            monthly_changes.append(monthly_change)

        # Track greatest increase and decrease in profit
            if monthly_change > greatest_increase_in_profit[1]:
                greatest_increase_in_profit = [row[0], monthly_change]
            if monthly_change < greatest_decrease_in_profit[1]:
                greatest_decrease_in_profit = [row[0], monthly_change]

        previous_profit = int(row[1])

        # Calculate average change
    average_change = sum(monthly_changes) / len(monthly_changes)

    #printing and exporting
    #print
    print(f"Total Months: {Total_months}")
    print(f"Total: ${Total_net_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_in_profit[0]} (${greatest_increase_in_profit[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_in_profit[0]} (${greatest_decrease_in_profit[1]})")

# Export the analysis results to a text file
output_file = "financial_analysis.txt"
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {Total_months}\n")
    file.write(f"Total: ${Total_net_profit_loss}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_in_profit[0]} (${greatest_increase_in_profit[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_in_profit[0]} (${greatest_decrease_in_profit[1]})\n")
