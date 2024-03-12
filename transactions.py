# Account is empty (0) at the beginning of the year

# Card fee is 5 ( 5 * 12 -> Yearly ) per month unless there were 3 payments made by card for a total cost of at least 100

# Function solution takes 2 arguments, array A, transaction amounts and array D for transaction dates

# Compute the final balance at the end of the year

def solution ( A, D ) :
    monthly_fee = 5
    months = 12
    # Total -> to hold the total balance  as the program loops
    total = 0
    counter = 0

    for y in A :
        if A[y] < 0 :
            month1 = int(D[y].split('-')[1])
    #     for z in D :
    #         if D[y][5:6] == D[z][5:6] :
    #             counter = counter + 1
    # print ( f"counter : {counter}")

    if counter >= 3 :
        months = months - 1

    for x in A :
        total = total + x
        print ( total )
    
    # Deducting the specified monthly fee from the total balance
    grand_total = total - ( monthly_fee * months )
    print ( grand_total )
    return grand_total

# Test run
result = solution ([100, 100, 100, -10], ["2020-12-31","2020-12-22","2020-12-03", "2020-12-29"])