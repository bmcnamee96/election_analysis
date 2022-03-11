# import the dependencies
import csv
import os

# make a variable that has the file you are opening path
file_path = os.path.join("Resources", "election_results.csv")

#create a filename variable to direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the file and read the file
with open(file_path) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # print the header row
    headers = next(file_reader)
    print(headers)

    # print each row in the csv file
    # for row in file_reader:
    #     print(row)

    # The data we need to retrieve
    # 1. The total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the election based on popular vote

    # close the file after all analysis
    # print(election_data)
