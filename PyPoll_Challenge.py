# Add our dependencies
import csv
import os
# Create a filename variable to a direct or indirect path to the resources and final output
file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")
#create the Counter of Total Votes
total_votes = 0
# Create the county and candidate list, county-votes and candidates-votes dictionary
county_list = []
county_votes = {}
candidate_list = []
candidate_votes = {}
#Create a county turnout and winning count trackers
largest_turnout_county = ""
largest_turnout_count = 0
largest_turnout_percentage = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results csv and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers=next(file_reader)
#Analysis of the election_results file
    for row in file_reader:
        #Add a vote per ballot
        total_votes += 1
#Read the county name per ballot and Creates Unique list of Countys with corresponding turnover.
        county_name = row[1]
        if county_name not in county_list:
           county_list.append(county_name)
           county_votes[county_name]=0
        county_votes[county_name]+=1  
#Read the candidate name per ballot and creates Unique list of Candidates with corresponding votes.
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
#Save total votes results, print to terminal and add to the text file
    with open(file_to_save,"w") as txt_file:
        election_results = (
        f'\n'
        f'Elections Results\n'
        f'-------------------\n'
        f'Total Votes = {total_votes:,}\n'
        f'-------------------\n'
        f"\n"
        f"County votes:\n"
        )
        print(election_results,end="")
        txt_file.write(election_results)
#Determine county's result
        for county in county_votes:
            cvotes = county_votes[county]
            cvotes_percentage = int(cvotes)/int(total_votes)*100
            if (cvotes > largest_turnout_count) and (cvotes_percentage > largest_turnout_percentage):
                largest_turnout_count = cvotes
                largest_turnout_percentage = cvotes_percentage
                largest_turnout_county = county
#Save county's results to our text file and terminal
            county_results=(f"{county}: has {cvotes_percentage:.2f}% of the votes ({cvotes:,} votes)\n")
            print(county_results,end="")
            txt_file.write(county_results)
#Save the largest turnout county's results to our text file and terminal
        largest_turnout_summary=(
            f"\n"
            f"-----------------\n"
            f"Largest County Turnout: {largest_turnout_county}\n"
            f"-----------------\n"
            f"\n"
            f"Candidates results:\n"
        )
        print(largest_turnout_summary)
        txt_file.write(largest_turnout_summary)
#Determine percentage of votes per candidate
        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            vote_percentage = int(votes)/int(total_votes) * 100
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate
#Save the candidate results to our text file and terminal
            candidate_results=(f"{candidate}: has {vote_percentage:.2f}% of the votes ({votes:,} votes)\n")
            print(candidate_results,end="")
            txt_file.write(candidate_results)
#Save the winning results to our text file and terminal
        winning_candidate_summary = (
            f"\n"
            f"-----------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning vote count: {winning_count:,} out of {total_votes:,} votes\n"
            f"Winning percentage: {winning_percentage:.2f}%\n"
            f"-----------------\n"
        )
        print(winning_candidate_summary,end="")
        txt_file.write(winning_candidate_summary)
#End of challenge