"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.
    Also performs error handling for cases where a user manually creates an account and provides invalid inputs.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    if (type(balance) == float or type(balance) == int)  and (type(interest_rate) == float or type(interest_rate) == int) and type(months) == int:
        interest_filler = 0
        user_CD = Account(balance, interest_filler)

        # Calculate interest earned
        interest_earned = balance * ((interest_rate/100)*(months/12))

        # Update the CD account balance by adding the interest earned
        updated_balance = user_CD.balance + interest_earned

        # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
        user_CD.set_balance(updated_balance)

        # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
        user_CD.set_interest(interest_earned)

        # Return the updated balance and interest earned.
        return  user_CD.balance, user_CD.interest
    else:
        error_string = ""
        if not (type(balance) == float or type(balance) == int):
            error_string += f"The balance your entered ({balance}) was not a number.\n"
        if not (type(interest_rate) == float or type(interest_rate) == int):
            error_string += f"The interest rate you entered ({interest_rate}) was not a number.\n"
        if not type(months) == int:
            error_string += f"The term you entered ({months}) was not an integer.\n"
        #The error string is returned with an additional empty quote to maintain output consistency
        return error_string, " "

if __name__ == "__main__":
    # Call the main function.
    print("\nShould return 1100, 100")
    print(create_cd_account(1000, 10, 12))

    print("\nShould tell you that your balance wasn't a number.")
    print(create_cd_account('bob', 10, 12))
