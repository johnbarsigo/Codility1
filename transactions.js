// Account is empty (0) at the beginning of the year

// Card fee is 5 ( 5 * 12 -> Yearly ) per month unless there were 3 payments made by card for a total cost of at least 100

// Function solution takes 2 arguments, array A, transaction amounts and array D for transaction dates

// Compute the final balance at the end of the year


function solution ( A, D ) {
    let total;
    let monthlyFee = 5;
    let x = 0;
    let months = 12;

    // A for loop to iterate through the transaction dates checking for similar months
    // Let x to contain the months repeated

    for ( let i = 0; i < D.length; i++ ) {
        for ( let k = 0; k < D.length; k++) {
            // Checking the value of the strings D at index 5
            if ( D[i][5] === D[k][5] ) {
                // Checking to confirm the total is over or equal to 100 warranting a pass on the fee
                if ( (A[i] + A[k]) >= 100 ) {
                    x += 1;
                }
            }
        }
        //return x;
    }
    
    // If there exists a month with more than two card transactions over or equal to 100
    if ( x > 2 ) {
        months = months - 1;
    }

    // Total -> to hold the total balance  as the program loops
    for ( let j = 0; j < A.length; j++) {
        total += A[j];
        console.log ( A[j] );
    }
    // Deducting the specified monthly fee from the total balance
    let grandTotal = total - (monthlyFee * months );
    return grandTotal;
}

// Test
let testResult = solution ([100, 100, 100, -10], ["2020-12-31","2020-12-22","2020-12-03", "2020-12-29"]);
console.log ( testResult );