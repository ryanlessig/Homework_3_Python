#import modules for reading csv files and for different operating system file path formatting
import os
import csv

#set file path for the budget data csv file
budget = os.path.join('..', 'Resources', 'budget_data.csv')

#intialize counts for all the counters needed
num_of_months = 0

current_month_change = 0
total_month_change = 0
num_of_changes = 0

current_month_revenue = 0
previous_month_revenue = 0
total_revenue= 0

greatest_increase = 0
greatest_decrease = 0

greatest_increase_date = ""
greatest_decrease_date = ""

#open the csv file and start looping through it
with open(budget, 'r') as raw_data:

    #set csv_reader to the csv file and read it
    read_csv = csv.reader(raw_data, delimiter=',')

    #skip the header row
    csv_header = next(read_csv)

    #go to the next row and save the value in the second column as the current months revenue for use later in calculating changes
    #increase the number of months counter by 1
    #add the current months revenue value to the total revenue counter
    current_month_revenue = next(read_csv)
    previous_month_revenue = current_month_revenue[1]
    num_of_months += 1
    total_revenue += int(current_month_revenue[1])

    #start the for loop to read the remaining rows of the csv files
    #increase the number of months counter by 1
    #add the current months revenue value to the total revenue counter
    #do the math to find hte current month change and add the change to the total change
    #increase the number of changes counter by 1
    #set the previous month revenue variable equal to the current value in the second column
    for row in read_csv:
        num_of_months += 1
        total_revenue += int(row[1])
        current_month_change = int(row[1]) - int(previous_month_revenue)
        total_month_change += current_month_change
        num_of_changes += 1 
        previous_month_revenue = int(row[1])

        #if the current month increase is greater than the greatest increase then store that month and value into variables
        if(current_month_change > greatest_increase):
                greatest_increase = current_month_change
                greatest_increase_date = str(row[0])
        #if the current month decrease is less than the greatest decrease then store that month and value into variables
        if(current_month_change < greatest_decrease):
                greatest_decrease = current_month_change
                greatest_decrease_date = str(row[0])

#calculate the average change for all the months
average_change = round(total_month_change / num_of_changes, 2)

#print the output to terminal
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {str(num_of_months)}")
print(f"Total Revenue: ${str(total_revenue)}")
print(f"Average Change: ${str(average_change)}")
print(f"Greatest Increase in Profits: {str(greatest_increase_date)} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {str(greatest_decrease_date)} (${str(greatest_decrease)})")

#Write output to text file
#set the output path and file name
output_path = os.path.join("Output", "PyBank_Output.txt")

#open the file in read mode and print the output
with open(output_path, 'w') as text_file:

    text_file.write("Financial Analysis\n"),
    text_file.write("---------------------------\n")
    text_file.write(f"Total Months: {str(num_of_months)}\n")
    text_file.write(f"Total Revenue: ${str(total_revenue)}\n")
    text_file.write(f"Average Change: ${str(average_change)}\n")
    text_file.write(f"Greatest Increase in Profits: {str(greatest_increase_date)} (${str(greatest_increase)})\n")
    text_file.write(f"Greatest Decrease in Profits: {str(greatest_decrease_date)} (${str(greatest_decrease)})\n")