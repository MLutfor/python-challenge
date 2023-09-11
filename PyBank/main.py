import os
import csv

#Values for key variables will start off as zero or none as the program needs
#to look through the data set first
total_money=0 
months=0 #Variable to count each month
total_changes = 0 
previous_money = None 
greatest_decrease = None 
greatest_increase = None 


cereal_csv = "budget_data.csv"  #Name of the csv file with the dataset
output_file = "budget_data.txt" #Name of the output text file
 
greatest_increase_month = None 
greatest_decrease_month = None 

#Read through the csv file
with open(cereal_csv ) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Removes header being read from the dataset
    header=next(csv_reader)

    #Looks through each row in the dataset
    for r in csv_reader:
        
        months=months+1
        money=int(r[1]) #Look through each month for how much money was lost/gained
        total_money+=money  # Add the money from each month to the grand total of all months combined

        if previous_money is not None:  
                change = money - previous_money #Determine the money changes between every month
                total_changes += change #Total used to determine the average change for each month
            
                 # Check if this change is greater than the current greatest increase
                if greatest_increase is None or change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_month = r[0] #Stored month of greatest increase
                
                # Check if this change is smaller than the current greatest decrease
                if greatest_decrease is None or change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_month = r[0] #Stored month of greatest decrease


        previous_money = money #Stores the amount from the previous month to determine money changes in this for loop
        


average_change = total_changes / (months - 1)  # Calculate the average change

#With statement to write results into text file
with open(output_file, "w") as output_file:   
    
    #Print out results to terminal
    print(f"Financial Anaylsis")
    print(f"----------------------------")
    print(f"Total Months: {months}")
    print(f"Total : ${total_money:.2f}")
    print(f"Average Change: ${average_change:.2f}")
    
    print(f"Greatest Increase: {greatest_increase_month} (${greatest_increase:.2f})") 
    print(f"Greatest Decrease: {greatest_decrease_month} (${greatest_decrease:.2f})") 

    #Print out results to a text file
    output_file.write(f"Financial Anaylsis\n")
    output_file.write(f"----------------------------\n")

    output_file.write(f"Total Months: {months}\n")
    output_file.write(f"Total : ${total_money:.2f}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase: {greatest_increase_month} (${greatest_increase:.2f})\n")
    output_file.write(f"Greatest Decrease: {greatest_decrease_month} (${greatest_decrease:.2f})\n")

print(f"Results have been saved to budget_data.txt")
