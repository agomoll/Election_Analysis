# Election results audit data to gather:
    # Total number of votes cast
    # A complete list of candidates who receive votes
    # Total number of votes each candidate recceived
    # Percent of votes each candidate won
    # Winner of the election

import csv
import os
from tkinter import N

# assign a varable fo the file to load and the path for the csv.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to save the file to a path to a text file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize vote counter
total_votes = 0

# Initialize an empty list to hold candidate names
candidate_options = []

# Initialize an empty dictionary to hold candidates and their vote count
candidate_votes = {}

# Winning Candidate and Winning count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and Print the header row in the csv file
    headers = next(file_reader)
    #print(headers)

    # print each row in the CSV file.
    for row in file_reader:
        # Add to the total row
        total_votes += 1
        #Print candidate name from each row
        candidate_name = row[2]
        # Append candidate options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name) 
            # Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0   
        # Accumulate votes to the dictionary
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes: ,}\n"
        f"---------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate
    for candidate_name in candidate_votes:
                # Get vote count for each candidate
                votes = candidate_votes[candidate_name]
                #calulate the percentage of the total vote
                vote_percentage = float(votes) / float(total_votes) * 100
                # Print candidate name and percentage of vote
                candidate_results = (f"{candidate_name}: received {vote_percentage:.1f}% {votes: ,}\n")
                print(candidate_results)

                # Save to text file
                txt_file.write(candidate_results)

                # Test if votes and percentage are greater than what assigned
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                    # Assign votes and percentage if greater
                    winning_count = votes
                    winning_percentage = vote_percentage
                    winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")        
    print(winning_candidate_summary)      

    # Save winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)             
                        
                                    
    
    
    # Print total votes
    #print(total_votes)
    #Print candidate names
    #print(candidate_options)
    #print(f"Total votes: {total_votes}")
    #print(candidate_votes)


    

    # Using the with statement open the text file as a write file.
    #with open(file_to_save, "w") as txt_file:
    # write some data to the text file
        #txt_file.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")




    