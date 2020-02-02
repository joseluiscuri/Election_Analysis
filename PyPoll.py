# Data we need to retrieve:
# 1. Total number of votes
# 2. Complete list of candidates
# 3. Percentage of voter per candidate
# 4. Total votes for each candidate.
# 5. Winner of the election
# 
# Add our dependencies
import csv
import os
file_to_load = os.path.join('Resources','election_results.csv')
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file with the reader function. 
    file_reader = csv.reader(election_data)
    # Print each  Row in the CSV file
    #for row in file_reader:
    #    print(row[1:3])
    headers=next(file_reader)
    print(headers)
