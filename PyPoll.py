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

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

# write the code to the txt file
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    
    print(election_results, end="")

    # save the final vote count to the txt file
    txt_file.write(election_results)

    # determine the percentage of votes for each candidate by using a for loop
    # iterate through the candidate list
    for candidate_name in candidate_votes:
        
        # retrive vote count of a candidate
        votes = candidate_votes[candidate_name]

        # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # print the candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {round(vote_percentage, 1)}% ({votes:,})\n")
        # print the candidate results
        print(candidate_results)
        # save the candidate results to our text file
        txt_file.write(candidate_results)


        # determine winning vote count and candidate
        # determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # set the winning_candidate equal to the candidates name
            winning_candidate = candidate_name

    # Create a winning candidate summary
    winning_candidate_summary = (
        f"--------------------------\n" 
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count {winning_count:,}\n" 
        f"Winning Percentage: {winning_percentage:.1f}%\n" 
        f"--------------------------\n")
    # print the winning candidate summary
    print(winning_candidate_summary)
    # save the winning candidate summary to the txt file
    txt_file.write(winning_candidate_summary)
