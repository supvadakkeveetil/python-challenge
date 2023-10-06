#Program to find the Change in Profit and Loss, 
#Total Profit/Loss , Min and the Max Profit/Loss

#import modules
import os
import csv
total_months=0
total_profitloss=0
change_profitloss=0
# to create file paths across OS
csvpath = os.path.join("Resources", 'budget_data.csv')
previous_PL=0
Change=[]
Greatest_Inc_Profit=0
Greatest_Dec_Profit=0

# Reading the values in the csv file
with open(csvpath) as csvfile:
    # to read the csv file
    csvreader= csv.reader(csvfile, delimiter=',')
    # to store header row
    csvreader = csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    print(header)
    # to avoid appending the first row to the Change list
    first_row = next(csvreader)
    total_months +=1
    total_profitloss += int(first_row[1])
    previous_PL = int(first_row[1])


    for row in csvreader:
        # Track the total months and total profit/loss
        total_months += 1
        total_profitloss = total_profitloss + int(row[1])

        # Calculate the change in profit/loss
        change_profitloss = int(row[1]) - previous_PL
        previous_PL = int(row[1])
        Change.append(change_profitloss)

        # Calculate the greatest increase in profit/loss
        if change_profitloss > Greatest_Inc_Profit:
            Greatest_Inc_Profit = change_profitloss
            Date_Inc = row[0]

        # Calculate the greatest decrease in profit/loss
        if change_profitloss < Greatest_Dec_Profit:
            Greatest_Dec_Profit = change_profitloss
            Date_Dec = row[0]
      
      # to find the average change 
    average_profitloss = sum(Change)/len(Change)
    
# Printing results to console and also storing output to a text file 
output_text_file=os.path.join("Analysis", 'Budget_Analysis.txt')
with open(output_text_file,"w") as textfile:
    
    Financial_Analysis = ("\nFinancial Analysis \n" "-------------------------\n" f"\n Total Months: {total_months:,}\n""\n Total:" + "  $" + str(total_profitloss))
    print(Financial_Analysis)
    textfile.write(Financial_Analysis)
    Average = (f"\n \n Average Change :" + " $" + str(round((average_profitloss),2)))
    print(Average)
    textfile.write(Average)
    Greatest_Change = ("\n \n Greatest Increase in Profits:" + "  " + str(Date_Inc) + " ($" + str(Greatest_Inc_Profit)) + ")" +  ("\n \n Greatest Decrease in Profits:" + "  " + str(Date_Dec) +  " ($" +str(Greatest_Dec_Profit) +")" ) 
    print(Greatest_Change)
    textfile.write(Greatest_Change)
