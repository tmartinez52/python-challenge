import os 
import csv

# location of the budget file
csvpath = os.path.join("..", "Resources", "budget_data.csv")
outputfile = "budget.txt"

months = []
months_revenue = []
total_revenue = 0

greatest_increase = 0
greatest_decrease = 0
increase_month = 0
decrease_month = 0


with open(csvpath, "r") as infile:
    csv_reader = csv.reader(infile, delimiter=",")
    csv_header = next(csv_reader)
    for month,revenue in csv_reader:
        months.append(month)
        months_revenue.append(revenue)


counter = 0
for revenue in months_revenue:
    if counter == 0:
        greatest_increase = revenue
        greatest_decrease = revenue
    else :
        if revenue > greatest_increase:
            greatest_increase = revenue
            increase_month = counter
            
        if revenue < greatest_decrease:
            greatest_decrease = revenue
            decrease_month = counter
    counter += 1
    total_revenue += int(revenue)


average_revenue = total_revenue / len(months)


text_output = (f"""
Financial Analysis
-----------------------
Total Months: {len(months)}
Total: ${total_revenue}
Average Change: {average_revenue}
Greatest Increase in Profits: {months[increase_month]} ${greatest_increase}
Greatest Decrease in Profits: {months[decrease_month]} ${greatest_decrease}
""")



with open(outputfile, "w", newline="") as datafile:
    datafile.write(text_output)




