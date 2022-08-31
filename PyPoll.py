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
 
# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join(path, "analysis", "election_analysis.txt")


# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.

    txt_file.write("Counties in the Election\n ---------------\nArapahoe\n Denver\n Jefferson.")


# Open the election results and read the file.

with open(file_to_load) as election_data:

# To do: perform analysis.

    # Read the file object with the reader function.

    file_reader = csv.reader(election_data)

     # Print header row in the CSV file.

    headers = next(file_reader)

    print(headers)