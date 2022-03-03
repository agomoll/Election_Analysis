import csv
import os

# assign a varable fo the file to load and the path for the csv.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to save the file to a path to a text file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and Print the header row in the csv file
    headers = next(file_reader)
    print(headers)




# Using the with statement open the text file as a write file.
with open(file_to_save, "w") as txt_file:
# write some data to the text file
    txt_file.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")




# Total number of votes cast
# A complete list of candidates who receive votes
# Total number of votes each candidate recceived
# Percent of votes each candidate won
# Winner of the election


