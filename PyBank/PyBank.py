
# Dependencies

import os

import csv



# request file names for input and output, declair the subfolder for holding the input data

input_file = input(" Please enter the name of the data file (with csv ext): ")

csvpath = os.path.join("raw_data", input_file)

output_file = input("Please enter the name of the Text file to hold the Financial Review (with txt ext): ")





# Declaration of variables that will be utilized during the looping and output process



month_count=0

total_revenue=0

lrg_loss=0

loss_date="unknown"

gain_date="unknown"

lrg_gain=0

avg_delta = 0

current_month_rev=0

prior_month_rev=0

delta=0



#looping process to gather the output information that fills the variables 

#skips the first month for calculating the monthly change (exclude) keeps a 

#running tab of months and revenue.  



with open(csvpath) as revenue_data:

    reader = csv.DictReader(revenue_data)

    for row in reader:

        prior_month_rev=current_month_rev 

        if prior_month_rev==0:

            exclude=int(row["Revenue"])

        total_revenue=total_revenue+ int(row["Revenue"])

        month_count = month_count + 1

        # calculates the change in current month revenue and keeps total     

        current_month_rev=int(row["Revenue"])

        delta=current_month_rev-prior_month_rev

        avg_delta=avg_delta+delta

        # flags the largest loss or largest gain

        if delta > lrg_gain:

            lrg_gain=delta

            gain_date=row["Date"]

        elif delta < lrg_loss:

            lrg_loss=delta

            loss_date=row["Date"]

        

#calculates the average change over the period

avg_delta=avg_delta-exclude

delta_percentage=avg_delta/(month_count-1)



#outputs the results and closes the output file



text_file = open(output_file, "w")

print("  ")

text_file.write(" \n")

print("--------------------------------------------------------------------")

text_file.write("-------------------------------------------------------------------- \n")

print(" Financial Analysis")

text_file.write("  Financial Analysis \n")

print("--------------------------------------------------------------------")

text_file.write("-------------------------------------------------------------------- \n")

print("Total number of months in period: " + str(month_count))

text_file.write("Total number of months in period: " + str(month_count) + "\n")

print("Total Revenue in period: $ " + str(total_revenue))

text_file.write("Total Revenue in period: $ " + str(total_revenue) + "\n")

print("Average monthly change in Revenue : $" + str(delta_percentage))

text_file.write("Average monthly change in Revenue : $" + str(delta_percentage) + "\n")

print("Greatest monthly increase in Revenue : " + str(gain_date) + "   $ " + str(lrg_gain))

text_file.write("Greatest monthly increase in Revenue : " + str(gain_date) + "   $ " + str(lrg_gain) + "\n")

print("Largest monthly decrease in Revenue : " + str(loss_date) + "   $ " + str(lrg_loss))

text_file.write("Largest monthly decrease in Revenue : " + str(loss_date) + "   $ " + str(lrg_loss) + "\n")

print("--------------------------------------------------------------------")

text_file.write("-------------------------------------------------------------------- \n")

text_file.close()
