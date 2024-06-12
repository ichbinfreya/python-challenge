# This is a python challenge about two companies: PyBank and PyPoll.
At the start of the Python week, the basics of the command-line interface (CLI) was introduced. 
Visual Studio Code is a source-code editor. Python is installed and launched. 
It begins with expoloring basic functionality: variables, comditionals, and loops.

For this challenge, I firstly created a repository called python-challenge.
Then, I clone it to my local computer.
  'git clone https://github.com/ichbinfreya/python-challenge.git
  
  touch PyBank/ .gitkeep
  touch PyPoll/ .gitkeep
  
  git commit -m "Created PyBank and PyPoll directories"
  
  git push origin master'
  
To create a file, use 'touch' command.
To open the python file, use 'explorer xxx.py' or 'code xxx.py'
  
CSV definition
The csv module in Python is a built-in library that provides functionality for reading and writing data in CSV (Comma-Separated Values) format. CSV files are commonly used to store tabular data, where each line of the file corresponds to a row in the table, and each field in the row is separated by a delimiter, typically a comma.

CSV features and instruction
1. Reading CSV Files:
  Read CSV files and convert them into lists or dictionaries for further processing.
2. Writing to CSV Files:
  Write lists or dictionaries into CSV files.
3. Handling Different Delimiters:
  While the default delimiter is a comma, the csv module can handle other delimiters such as tabs or semicolons.
  
For example, you can see the data in .csv file is:
Voter ID,County,Candidate
12864552,Marsh,Charles Casper Stockham


When you read the csv file with 'csv.reader' command, each row will be represented as a list of strings:
['12864552', 'Marsh', 'Charles Casper Stockham']

Therefore, the candidate is at column three in the current row.
If you want to assign a value to the candidate, then:
candiate = row[2]

Default command
  import csv 
  #You can use the csv functions by importing csv
  
  with open(file_path, mode='r') as file:
  # This opens the file specified by file_path in read mode ('r'). The with statement ensures that the file is properly closed after its suite
  finishes.
  
  reader = csv.reader(file, delimiter=',')
  #This creates a csv.reader object which will iterate over lines in the given CSV file.
  
  header = next(reader)
  #This reads the first row from the CSV file, which is typically the header row containing the column names.

  for row in reader:
    print(row)
  #This iterates over the remaining rows in the CSV file. Each row is a list of values corresponding to the fields in that row.
