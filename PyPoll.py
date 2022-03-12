# import the dependencies
import csv
from functools import total_ordering
import os

# make a variable that has the file you are opening path
file_path = os.path.join("Resources", "election_results.csv")

#create a filename variable to direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# total vote counter variable set = 0
total_votes = 0

# make a candidate options list
candidate_options = []

# make a dictionary for the candidate votes
candidate_votes = {}

# open the file and read the file
with open(file_path) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read and skip the header row
    headers = next(file_reader)

    # print each row in the csv file
    for row in file_reader:
        # incremement total votes by 1
        total_votes += 1

        # print the candidate name from each row
        candidate_name = row[2]

        # if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            # add the name to the list
            candidate_options.append(candidate_name)

            # track the candidates vote count
            candidate_votes[candidate_name] = 0

        # add 1 for every vote that the candidate gets
        candidate_votes[candidate_name] += 1

# determine the percentage of votes for each candidate by using a for loop
# iterate through the candidate list
for candidate_name in candidate_votes:
    
    # retrive vote count of a candidate
    votes = candidate_votes[candidate_name]

    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #print the candidate name and percentage of votes
    print(f"{candidate_name}: received {round(vote_percentage, 2)}% of the votes.")

# print the total votes variable
print(total_votes)

# print the candidate list
print(candidate_options)

# print the candidates votes
print(candidate_votes)


# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
