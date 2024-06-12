# Import a csv module
import csv

# Path to the CSV file
file_path = 'election_data.csv'

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Open and read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)  # Skip the header row

    for row in reader:
        total_votes += 1
        candidate = row[2] # When reading the csv file with 'csv.reader', each row is represented as a list of strings
        # This is used to assign the value from the third column, which is the 'candidate' column, of the current row to variable 'candidate'

        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

# Calculate percentage of votes for each candidate who won
candidate_results = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidate_results[candidate] = {"percentage": percentage, "votes": votes} # Dictionary consists of {"key":: value, "key": value}
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Optimize the result
results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, data in candidate_results.items():
    results += f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n"
results += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the results to the console
print(results)

# Export the results to a text file
output_file_path = 'election_results.txt'
with open(output_file_path, mode='w') as file:
    file.write(results)