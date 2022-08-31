# THe data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received voted
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
import os
# Assign a variable for the file to load and the path.


#path requires 'r' to find path 
path = r"C:\Users\wero\Desktop\Bootcamp\UT-VIRT-DATA-PT-08-2022-U-B - workfile\Election_Analysis"

file_to_load = os.path.join(path, "Resources", "election_results.csv")
 

# Create a filename variable to save a direct or indirect path to the file.
file_to_save = os.path.join(path, "analysis", "election_analysis.txt")


# Initialize a total vote counter.
total_votes = 0


#candidate options
candidate_options = []


#declare empty dictionary
candidate_votes = {}


# Winning Candidate and Winning Count Tracker
winning_candidate = ""

winning_count = 0

winning_percentage = 0


# Open the election results and read the file.

with open(file_to_load) as election_data:

# To do: perform analysis.

    # Read the file object with the reader function.

    file_reader = csv.reader(election_data)

     # Print header row in the CSV file.

    headers = next(file_reader)



 #Print each row in the CSV file.
    for row in file_reader:

  #Add to the total of vote count
        total_votes += 1

# Print the candidate name from each row.
        candidate_name = row[2]


# If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add to list of candidates

            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# Open file to write
with open(file_to_save, "w") as txt_file:


    # Print the final vote count to the terminal.
    election_results = (
    f"\nElection Results\n"

    f"-------------------------\n"

    f"Total Votes: {total_votes:,}\n"
    
    f"-------------------------\n")

    print(election_results, end = "")

    txt_file.write(election_results)

    for candidate_name in candidate_options:

        # Retrieve vote count of a candidate.
        votes =  candidate_votes[candidate_name]

        # Calculate the percentage of votes.

        vote_percentage = float(votes) / float(total_votes) * 100


        #Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            #If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # Set the winning_candidate eqaul to the candidate's name.

            winning_candidate = candidate_name

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)

    winning_candidate_summary = (

        f"-------------------------\n"

        f"Winner: {winning_candidate}\n"

        f"Winning Vote Count: {winning_count:,}\n"

        f"Winning Percentage: {winning_percentage:.1f}%\n"

        f"-------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)

