import os
import csv

def percentage(part, whole):
  return 100 * float(part)/float(whole)


csvpath = os.path.join("..", "Resources", "election_data.csv")
ouputfile = "election.txt"

# declaring lists
voter_id = []
county = []
candidate = []
# declaring vote variables
votes = 0
votes_for_li = 0
votes_for_correy = 0
votes_for_khan = 0
votes_for_o_tooley = 0
# declaring percent variables
percent_for_li = 0
percent_for_correy = 0
percent_for_khan = 0
percent_for_o_tooley = 0
# declaring winner
winner = ""

# extracting data from csv file
with open(csvpath, "r") as infile:
    csv_reader = csv.reader(infile, delimiter=",")
    csv_header = next(csv_reader)
    for Voter_ID, County, Candidate in csv_reader:
        voter_id.append(Voter_ID)
        county.append(County)
        candidate.append(Candidate)
        votes += 1
infile.close()

# counting votes
counter = 0
for vote in candidate:
    if vote == "Khan":
        votes_for_khan += 1
    elif vote == "Correy":
        votes_for_correy += 1
    elif vote == "Li":
        votes_for_li += 1
    else :
        votes_for_o_tooley += 1

#finding popular vote
candidate_votes = [votes_for_li, votes_for_correy, votes_for_khan, votes_for_o_tooley]
popular_candidate = max(candidate_votes)

#finding winner
if popular_candidate == votes_for_li:
    winner = "Li"
elif popular_candidate == votes_for_correy:
    winner = "Correy"
elif popular_candidate == votes_for_khan:
    winner = "Khan"
else:
    winner = "O'Toonley"

# calculating percentages
percent_for_li = percentage(votes_for_li, votes)
percent_for_correy = percentage(votes_for_correy, votes)
percent_for_khan = percentage(votes_for_khan, votes)
percent_for_o_tooley = percentage(votes_for_o_tooley, votes)

# generating output for file
text_output = (f"""
Election Results
----------------------
Total Votes: {votes}
----------------------
Khan: {percent_for_khan} ({votes_for_khan})
Correy: {percent_for_correy} ({votes_for_correy})
Li: {percent_for_li} ({votes_for_li})
O'Tooley: {percent_for_o_tooley} ({votes_for_o_tooley})
----------------------
Winner: {winner}
----------------------
""")

# file output
with open(ouputfile, "w", newline="") as datafile:
    datafile.write(text_output)




