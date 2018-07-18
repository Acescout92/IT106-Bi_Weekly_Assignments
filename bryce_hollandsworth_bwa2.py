#-------------------------------------------------------------------------------
# bryce_hollandsworth_bwa2.py
# Student Name: Bryce Hollandsworth
# Python version: 3.6
# Submission Date: 03/06/2018
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References:
#-------------------------------------------------------------------------------
# Notes to grader:
#-------------------------------------------------------------------------------
# Pseudocode:
#Implement main menu, accept standard inputs 1 or 2 for payoff summary or detailed summary, respectively
#If 1, call function credit_payoff
#If 2, call function detailed
#credit_payoff:
#   Request standard inputs for current balance, apr, and present menu
#   Menu: Request standard inputs for choices: Interest on current balance + 1% or 2% * current balance
#       If 1: calculate minimum payment using: interest = current_balance * (apr/12), min_payment = interest + (.01 * current_balance)
#           Declare month iterator and interest summation variables
#           Initialize while loop for while current balance > 0
#           subtract minimum payment from current balance, add back interest
#           Iterate month counter, add current interest rate to interest summation variable
#           Check if minimum payment > 15, if false minimum payment = 15
#           When current balance < 0, break from loop and print the month iterator and interest summation variable
#       If 2: Same as option 1, but determine minimum payment via: interest = current_balance * (apr/12), min_payment = .02 * current_balance, principal = min_payment - interest
#           Subtract principal from current balance instead of option 1 which subtracted the minimum payment
#           Print the same results as option 1
# detailed:
#   Same standard inputs as credit_payoff
#   Same menu as credit_payoff
#   Same formulas as credit_payoff
#   In the same calculation loops, add a print statement for month, interest paid, the minimum payment, the principal paid, and the remaining balance
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------
def main():
    """Implements the Main Menu"""
    choice = int(input("\tMain Menu:\n\t1)\tCredit Card Payoff Summary\n\t2)\tCredit Card Payoff Details\n\t3)Exit\n"))
    if choice == 1:
        credit_payoff() #calls credit_payoff function
    elif choice == 2:
        detailed() #calls the detailed summary function
    else:
        exit()

def credit_payoff():
    """Calculates the number of months and total interest paid given current balance and the apr"""
    month_count = 0 #month iterator
    interest_sum = 0 #interest summation to be used in calculation loop
    #Standard inputs:
    current_balance = float(input("Input current balance: "))
    apr = float(input("Input Annual Percentage Rate (APR): "))
    choice = int(input("\tPayoff Summary Menu:\n\t1)Interest on current balance +1%on current balance\
                       \n\t2)2% Of Current Balance\n")) #Secondary menu
    if choice == 1: #Secondary menu option 1
        while current_balance > 0: #Calculation loop, uses the first formula to calculate minimum payment
            interest = current_balance * (apr/12)
            min_payment = interest + (.01 * current_balance)
            if min_payment > 15: #checks if minimum payments is still greater than 15
                current_balance -= min_payment
                current_balance += interest
            else:
                min_payment = 15 #hardcoded minimum payment amount for when min_payment < 15
                current_balance -= min_payment
                current_balance += interest
            interest_sum += interest
            month_count += 1
        years = month_count/12
        print("\nSummary:\n-# years required to payoff card: ", round(years, 1),
              "\n-Total interest paid: ", round(interest_sum, 2))
    elif choice == 2:
        while current_balance > 0: #Calculation loop, uses the second formula to calculate minimum payment
            interest = current_balance * (apr/12)
            min_payment = .02 * current_balance
            principal = min_payment - interest
            if min_payment > 15: #Checks if min_payment > 15
                current_balance -= principal
            else:
                min_payment = 15 #hardcoded value for min_payment if min_payment < 15
                principal = min_payment - interest
                current_balance -= principal
            interest_sum += interest #adds current interest amount to interest summation variable
            month_count += 1 #iterate month by 1
        years = month_count / 12 #determine number of years
        print("\nSummary:\n-# years required to payoff card: ", round(years, 1),
              "\n-Total interest paid: ", round(interest_sum, 2)) #Final standard output

def detailed():
    """Prints a table of values that show month, interest, minimum payment, principal paid, and the remaining balance"""
    n = 11 #used in formatting
    month_count = 0 #iterator for total months
    interest_sum = 0 #variable that holds the sum of interest over every month
    current_balance = float(input("Input current balance: ")) #standard inputs
    apr = float(input("Input Annual Percentage Rate (APR): "))
    choice = int(input("\tPayoff Summary Menu:\n\t1)Interest on current balance +1% on current balance\
                           \n\t2)2% Of Current Balance\n")) #implements secondary menu
    if choice == 1: #calculator for option 1
        print("Month\t\t\tMinPay\t\t\tIntPaid\t\t\tPrincPaid\t\t\tRemBal") #builds table columns
        while current_balance > 0: #Condition: current_balance does not fall below 0
            #Formula 1:
            interest = current_balance * (apr/12)
            min_payment = interest + (.01 * current_balance)
            principal = min_payment - interest
            if min_payment > 15:
               current_balance -= min_payment
               current_balance += interest
            else:
                min_payment = 15
                current_balance -= min_payment
                current_balance += interest
            interest_sum += interest
            month_count += 1
            print(month_count, ' '*n, round(min_payment,2), 
                 ' '*n, round(interest, 2), ' '*n, round(principal,2), ' '*n, round(current_balance, 2))
        years = month_count/12
        print("\nSummary:\n-# years required to payoff card: ", round(years, 1),
              "\n-total interest paid: ", round(interest_sum, 2))
    elif choice == 2:
        print("Month\t\t\tMin.Pay\t\t\tint.paid\t\t\tprinc.paid\t\t\tcurrent_balance") #Creates table columns
        while current_balance > 0:
            #Formula 2:
            interest = current_balance * (apr / 12)
            min_payment = .02 * current_balance
            principal = min_payment - interest
            if min_payment > 15:
                current_balance -= principal #This formula uses the principal instead of the minimum payment
            else:
                min_payment = 15
                principal = min_payment - interest
                current_balance -= principal
            interest_sum += interest #Add interest to interest summation variable
            month_count += 1
            print(month_count, ' '*n, round(min_payment,2), ' '*n, round(interest,2),
            ' '*n, round(principal,2),' '*n, round(current_balance,2)) #Prints each variable under their respective columns
        years = month_count / 12 #Convert months to years
        print("\nSummary:\n-# years required to payoff card: ", round(years, 1),
              "\n-Total interest paid: ", round(interest_sum, 2))

main()