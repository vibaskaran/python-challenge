# Dependencies
# --------------------------------------
import csv

# Files to Load / Output
# --------------------------------------
file_to_load = "raw_data/election_data_2.csv"
file_to_output = "output/election_analysis_2.txt"

# Variables to Track

candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
total_votes = 0
greatest_vote_candidate = ""
greatest_vote_percentage = 0

# Main Process 
# --------------------------------------
# Reading the file
with open(file_to_load) as election_data:
  reader = csv.DictReader(election_data)

  # For Each row...
  for row in reader:

    # Total Votes
    total_votes = total_votes + 1

    # Build our Array of Unique Candidates 
    if row["Candidate"] not in candidate_options:

      # Add the candidate as an option
      candidate_options.append(row["Candidate"])

      # Set that candidate's initial vote count to 0
      candidate_votes[row["Candidate"]] = 0

    # If the candidate is NOT unique
    candidate_votes[row["Candidate"]] =  candidate_votes[row["Candidate"]] + 1
  print()
  print('Election Results')
  print('----------------------------')
  print('Total Votes: ',total_votes )
  print('----------------------------')
  with open(file_to_output, "w") as txt_file:
    txt_file.write('Election Results')
    txt_file.write("\n")
    txt_file.write('----------------------------')
    txt_file.write("\n")
    txt_file.write('Total Votes: '+ str(total_votes))
    txt_file.write("\n")
    txt_file.write('----------------------------')
    txt_file.write("\n")
  # Iterate through the candidate_votes
  for candidate in candidate_votes:

    votes = candidate_votes[candidate]
    vote_percentage = round((votes / total_votes) * 100,2)

    print(candidate +' ' + str(vote_percentage)+'% ('+str(votes)+')')
    with open(file_to_output, "a") as txt_file:
      txt_file.write(candidate +' ' + str(vote_percentage)+'% ('+str(votes)+')')
      txt_file.write("\n")

    if(vote_percentage > greatest_vote_percentage):

      greatest_vote_candidate = candidate
      greatest_vote_percentage = vote_percentage

  # Printing The Winner
  print('----------------------------')
  print("Winner: " + greatest_vote_candidate)
  print('----------------------------')
  # Output Files
  with open(file_to_output, "a") as txt_file:
     txt_file.write('----------------------------')
     txt_file.write("\n")
     txt_file.write('Winner: ' + greatest_vote_candidate)
     txt_file.write("\n")
     txt_file.write('----------------------------')
     txt_file.write("\n")


    
    