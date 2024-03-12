# CLASS DISCUSSION

# Given an array A of transactions and array D of transaction dates
# When all transactions have been added with deductions
# Then find the final account balance at the end of the year

# Conditions
# 1. Calculating the service charge = 5 per month unless three payments per month (-ve values) totaled >=100
# Assuming the acc. balance at the beginning of the year is 0


# Pseudocode
# A = [100, 100, 100, -10] = 290 (before service charge)
# D = ["2020-12-31","2020-12-22","2020-12-03", "2020-12-29"]
# 290 - service_charge = balance

# Variables
# amount_after_transactions == sum of values in A == 290
# service_charge
# chargeable_months = 12

# loop through all transactions
# if transaction A[i] is -ve
#    check the month in D[i]
#        D[i].split('-')[1]

# We need to know 1. month
#                 2. no of card payments
#                 3. total payments
# Create a dict (payment_tracker) of related info (above)

# Record transaction in payment_tracker (the above dict)
# if month exists in payment_tracker, update the no. of card payments and total expenditure
# Loop through the payment_tracker & for every month with >=3 card payments totalling >=100, there's no service charge
#       if card_payments > 2 && expenditure_total <= -100
#           chargeable_months -= 1
# Calculate the service charge
# deduct service_charge from the amount_after_transactions