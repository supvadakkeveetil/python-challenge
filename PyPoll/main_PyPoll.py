#Program to find the Election Data 
#Total Votes , Winner

# to create file paths across OS
import os
import csv
import contextlib
total_votes=0
winner_votes=0
csvpath = os.path.join('..', "Resources", 'election_data.csv')
output_text_file=os.path.join('..', "Resources", 'Election_Analysis.txt')
# List of Candidates and Votes
Candidate_List ={}

# Reading the values in the csv file

with open(csvpath) as csvfile:
    csvreader= csv.DictReader(csvfile, delimiter=',')
    
    for row in csvreader:
        total_votes= total_votes+1
        candidate =row["Candidate"]
        #use the keys() method to get all the keys from the Candidate_List dictionary
        #if the name is not in the list add the candidate name and set the vote count to 1 else increment the candidates vote count
        if candidate not in Candidate_List.keys():
            Candidate_List[candidate] = 1
            
        else :
            Candidate_List[candidate] += 1

with open(output_text_file,"w") as textfile:
 Election_Result =("\nElection Results\n" "-------------------------\n" f"\n Total Votes: {total_votes:,}\n" "\n-------------------------\n")

 print(Election_Result)
 textfile.write(Election_Result)


# to get each candidates vote count and then the percentage votes
 for candidate in Candidate_List:
     Candidate_votes= Candidate_List[candidate]  
     Percentage_votes= round((((Candidate_votes)/(total_votes)) *100),3)
     Participating_candidates = (f"\n {candidate}: {Percentage_votes}% ({Candidate_votes})\n")
     print(Participating_candidates)
     textfile.write(f"{Participating_candidates}")

   
    # finding the winning candidate with highest votes
     if(Candidate_votes)> winner_votes:
         Winner_Candidate_name = candidate
         winner_votes = Candidate_votes
 
 Winner= ("\n-------------------------\n" f"\n Winner: {Winner_Candidate_name}\n" "\n-------------------------\n")
 print(Winner)
 textfile.write(Winner)
