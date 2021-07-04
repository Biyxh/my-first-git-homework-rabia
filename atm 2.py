def display_balance():
    print("Your A/C balance is £{}".format(opening_balance))


def cash_withdraw(withdrawal_amount):
    global opening_balance

    print("Your A/C balance is £{}".format(opening_balance))
    opening_balance = opening_balance - withdrawal_amount
    print("Your current A/C balance is £{}")