#Game plan
    #Count the total number of votes cast
    #Compile complete list of candidates who received votes
    #Count the total number of votes each candidate won
    #Caluclate the percentage of votes each candidate won
    #Detirmine the winner of the election based on popular vote

# #import the CVS module and the os module
import os
import csv
# # In order to list what is in the module use dir(), example:
# # dir(csv)

# #Assign a variable for the file to load and the path.
file_to_load = os.path.join('resources', 'election_results.csv')
#Create a filename variable to an indirect path to the file.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read and analyze the data here.
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)


# #Using the open() function with the "w" mode, we will write data to the file
# with open(file_to_save, "w") as txt_file:

#     #Write some data to the file
#     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

