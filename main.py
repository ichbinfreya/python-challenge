# Import modules
import csv

# Path to the csv file, which is contained in the same parent folder.
file_path = 'budget_data.csv'

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
dates = []
greatest_increase = {"date": None, "amount": float('-inf')} # float('-inf') represents the negative infinity. I used float-point value which can contain negative sign. 
greatest_decrease = {"date": None, "amount": float('inf')}

# Open and read csv file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        date = row[0]  # First column in excel is date
        profit_loss = int(row[1])  # Second column is profit/losses

        # Increment total_months (the initialized variable) by 1 for each row
        total_months += 1

        # Add the profit/losses to the net_total
        net_total += profit_loss

        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss

            changes.append(change)
            dates.append(date)

            if change > greatest_increase["amount"]:
                greatest_increase = {"date": date, "amount": change}

            if change < greatest_decrease["amount"]:
                greatest_decrease = {"date": date, "amount": change}
        
        # Update previous_profit_loss for the next iteration
        previous_profit_loss = profit_loss

if changes:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Changes: ${average_change:.2f}") #': .2f' is to make the result with 2 decimals
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Optimize the result and export it as a text file
results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the results to the console
print(results)

# Export the results to a text file
output_file_path = 'financial_analysis.txt'
with open(output_file_path, mode='w') as file:
    file.write(results)