print("Welcome to Python Bank")
Trials = 3
UserPin = 1234


class UserExit:
    pass


while Trials != 0:
    Pin = int(input("Please Enter Your 4 digit Pin Number: "))
    if Pin != UserPin:
        Trials -= 1
        print("Wrong Pin Number, You Have", Trials, "Trials Left")
    else:
        UserChoice = input("e: Exit or w: Withdraw: ")
        if UserExit == "e":
            print("Thank you for using Python Bank")
            break
        if UserChoice == "w":
            UserWithdraw = opening_balance = 100
            input("Enter the number you would like to withdraw: ")
            number = int(input("Enter a number in the range of 1-100"))

            try:
                if number < 1 or number > 100:
                    raise Exception

                subtraction_result: int = 100 - number
                print(subtraction_result)

            except:
                print('Sorry more than £100 is unavailable in your Account')

            x = 100
            if x > 100:
                raise Exception("Sorry no transactions above £100")

            UserExit = input("Would  You Like to Continue? Y/N: ")
            if UserExit == "N":
                print("Thank you for using Python Bank")
                break
            else:
                continue

