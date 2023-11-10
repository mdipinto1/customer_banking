# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("\nPlease enter the starting balance of your savings account. "))
    savings_interest = float(input('Please enter the interest rate of your savings account. '))
    savings_maturity = int(input('Please enter the number of months your account will accrue interest over. '))

    # Call the create_savings_account function and pass the variables from the user.
    if all(var > 0 for var in (savings_balance, savings_interest, savings_maturity)):
        updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
        print(f"\nYour final balance after {savings_maturity} months will be ${updated_savings_balance:,.2f}.")
        print(f"Your earned interest on your original balance of ${savings_balance:,.2f} will be ${interest_earned:,.2f}.")

    #else statement for out of range variable catching
    else:
        print("One of the Savings Account variables entered was less than zero and therefore invalid")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("\nPlease enter the starting balance of your CD account. "))
    cd_interest = float(input('Please enter the interest rate of your CD account. '))
    cd_maturity = int(input('Please enter the number of months your account will accrue interest over. '))

    # Call the create_cd_account function and pass the variables from the user.
    if all(var > 0 for var in (cd_balance, cd_interest, cd_maturity)):
        updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

        # Print out the interest earned and updated CD account balance with interest earned for the given months.
        print(f"\nYour final balance after {cd_maturity} months will be ${updated_cd_balance:,.2f}.")
        print(f"Your earned interest on your original balance of ${cd_balance:,.2f} will be ${interest_earned:,.2f}.")

    else:
        print("One of the CD variables entered was less than zero and therefore invalid")

if __name__ == "__main__":
    # Call the main function.
    main()