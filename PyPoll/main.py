import os
import csv

#Lists will start empty as the program needs to look through the dataset first

candidates_full = []
candidate_count=[]
cereal_csv = "election_data.csv"  #Name of the CSV file with the dataset
output_file = "election_results.txt" #Name of the output text file
votes=0 #Value for total votes in the election



with open(cereal_csv ) as csv_file:
    #Delimiter separates the dataset into columns
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Removes header being read from the dataset
    header=next(csv_reader)
    
    #Looks through each row in the dataset
    for r in csv_reader:
        votes=votes+1 #variable to count total amount of votes

        #Third column in dataset has the candidate names
        candidate_name = r[2]

   
        if candidate_name not in candidates_full:
          
            candidates_full.append(candidate_name)
            # This counts the total vote for the candidate
            candidate_count.append(1)  # Initialize with 1 vote for the new candidate
        else:
            # Find the index of the candidate name in the list
            index = candidates_full.index(candidate_name)
            # Increment the vote count for that candidate
            candidate_count[index] += 1

#Print out total votes to terminal            
print(f"Election Results")   
print(f"-------------------------")          
print(f"Total Votes: {votes}")  
print(f"-------------------------") 

max_votes = max(candidate_count)  # Find the candidate with the maximum vote count 

# Find the index of the winner by matching the winner with the max vote count
winner_index = candidate_count.index(max_votes)  

#With statement to write results into text file
with open(output_file, "w") as output_file:
    
    #Print out total votes to text file
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {votes}\n")
    output_file.write("-------------------------\n")
    

    #Look though the full list of candidates to determine their votes count and percentage
    for i in range(len(candidates_full)):
    
        percentage = (candidate_count[i] / votes) * 100  # Calculate the percentage

        # Display the candidate name, vote count, and percentage.  3f leaves it to 3 decimal places
        print(f"{candidates_full[i]}:  {percentage:.3f}% ({candidate_count[i]})")
        output_file.write(f"{candidates_full[i]}:  {percentage:.3f}% ({candidate_count[i]})\n")
    
 
    #Display the name of the winner in both terminal and text file

    print(f"-------------------------") 
    print(f"Winner: {candidates_full[winner_index]}")
    print(f"-------------------------") 

    
    output_file.write(f"-------------------------\n")
    output_file.write(f"Winner: {candidates_full[winner_index]}\n")
    output_file.write(f"-------------------------\n")

