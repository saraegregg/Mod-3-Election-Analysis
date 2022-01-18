#Game plan
    #Count the total number of votes cast
    #Compile complete list of candidates who received votes
    #Count the total number of votes each candidate won
    #Caluclate the percentage of votes each candidate won
    #Detirmine the winner of the election based on popular vote

# #import the CVS module and the os module
import os
import csv

# Assign a variable to load a file from a path.
os.chdir(os.path.dirname(os.path.realpath(__file__)))
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a variable accumulator to count the total votes
total_votes = 0

#Declare a candidate list
candidate_options = []

#Declare a candidate vote count dictionary
candidate_votes = {}

#Initialize winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file:
    for row in file_reader:
            
        #Add +1 to total votes
        total_votes += 1

        #Get the candidates' names from the row and add it to the list if not already there
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Add candidate name as a key in the dictionary (later to add each vote under their name)
            candidate_votes[candidate_name] = 0
        
        #Add +1 to respective candidate vote total
        candidate_votes[candidate_name] += 1
    
    #Calculate each candidate's percentage of votes by:
    #Iterate through the candidate list
    for candidate_name in candidate_votes:

        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        #Calculate the percentage of votes:
        vote_percentage = (float(votes) / float(total_votes)) * 100

        #Determine winning vote count and candidate/determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true set winning_count = votes and winning_percentage = vote percentage and candidate's name to winning_candidate
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
        #Print the candidate name and percentage of votes.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #print the winning candidate, vote count, and percentage
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)