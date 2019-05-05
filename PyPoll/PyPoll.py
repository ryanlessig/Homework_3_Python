#Import modules for reading operation system specific requirements and handling CSV's
import os
import csv

#set the path for the election data csv file
election_data = os.path.join('..', 'Resources', 'election_data.csv')

#declare variables and initial dictionaries
num_of_votes_total = 0
most_votes = 0
candidate_dictionary= {}
percent_dictionary = {}

#open the csv file and start looping through it
with open(election_data, 'r') as csvfile:

    #set csv_reader to the csv file and read it
    csv_reader = csv.reader(csvfile, delimiter=',')

    #skip the header row
    csv_header = next(csv_reader)

    #for each row in the reader after the header, loop through them
    #increase the num_of_votes_total by 1 for each row
    #set the candidate name equal to the 2nd index (3rd column) of the csv file
    #check if the candidate name is already in the candidate dictionary
    #if the current candidate is not in the dictionary, place the candidate name in the dictionary with a value of 1 (vote count)
    #if the current candidate is already in the dictionary, increase the vote count by 1
    for row in csv_reader:
        num_of_votes_total += 1
        candidate_name = row[2]
        if candidate_name not in candidate_dictionary:
            candidate_dictionary[candidate_name] = 1
        else:
            candidate_dictionary[candidate_name] += 1

#for each canidate in the candidate dictionary, find their total amount of votes and divide that by the total number of votes in the election with a % format
for candidate_name, num_of_votes in candidate_dictionary.items():
    percent_dictionary[candidate_name]= '{0:.3%}'.format(num_of_votes/num_of_votes_total)

#for each candidate in the candidate dictionary, check if their number of votes is higher than the variable most_votes. If it is, store that number of votes into the most votes variable and set the winner candidate to the candidate name
#once this loops through all the candidates, it will find the candidate with the most votes
for candidate_name, num_of_votes in candidate_dictionary.items():
    if num_of_votes > most_votes:
        most_votes = num_of_votes
        winning_candidate = candidate_name

#create a comprehensive of the output for each candidate
candidate_summary_list = [f"{str(candidate_name)}: {str((percent_dictionary)[candidate_name])} ({str((num_of_votes))})" for candidate_name, num_of_votes in candidate_dictionary.items()]

#print the output to terminal                                       
print("Election Results")
print("---------------------------")
print(f"Total Votes: {str(num_of_votes_total)}")
print("---------------------------")
for candidate_stats in candidate_summary_list:
    print(f"{str(candidate_stats)}")
print("---------------------------")
print(f"Winner: {str(winning_candidate)}")
print("---------------------------")

#Write output to text file
#set the output path and file name
output_path = os.path.join("Output", "PyPoll_Output.txt")

#open the file in read mode and print the output
with open(output_path, 'w') as text_file:

    text_file.write("Election Results\n"),
    text_file.write("---------------------------\n")
    text_file.write(f"Total Votes: {str(num_of_votes_total)}\n")
    text_file.write("---------------------------\n")
    for candidate_stats in candidate_summary_list:
        text_file.write(f"{str(candidate_stats)}\n")
    text_file.write("---------------------------\n")
    text_file.write(f"Winner: {str(winning_candidate)}\n")
    text_file.write("---------------------------\n")