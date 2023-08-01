# you are a billionaire and have 10 days to spend all your money
# your name is John Bars, you do not have a wife, you repressed all your homosexuality

import random

money = 1000000000  # billion
days = 3
yes_no_list = ["yes", "no"]
buy_gam_don_list = ["buy", "gamble", "donate"]


# check that user enter a valid response
def string_checker(question, num_letters, valid_responses):

    if valid_responses == buy_gam_don_list:
        error = "please choose {} or {}".format(valid_responses[0], valid_responses[1], valid_responses[2])
    else:
        error = "please choose {} or {}".format(valid_responses[0], valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        responses = input(question).lower()

        for item in valid_responses:
            if responses == item[:short_version] or responses == item:
                return item

        print(error)


# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, output error
        if response == "":
            print("Sorry this cant be blank. Please Try again")
        else:
            return response


# check if value is a number
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an number value")


class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


print()
print(Color.RED + "UN-BILLIONAIRE" + Color.END)
print()


if string_checker(Color.YELLOW + "Do you want to read the instructions? (y/n): ", 1, yes_no_list) == "yes":
    print(Color.BLUE + "Instructions go here")  # fill out instructions

print(Color.END)

while days > 0:
    if days == 1:
        print(Color.YELLOW + "You have " + str(days) + " day to spend $" + str(money)+".")
    else:
        print(Color.YELLOW + "You have " + str(days) + " days to spend $" + str(money)+".")

    print("Choose wisely")
    print()
    print(">BUY")
    print(">GAMBLE")
    print(">DONATE")

    choice = string_checker(Color.YELLOW + "Choose: ", 1, buy_gam_don_list)

    if choice == "buy":
        print("You choose "+Color.GREEN+"'buy'")
        money -= 1000
    elif choice == "gamble":
        print("You choose "+Color.PURPLE+"'gamble'")
    elif choice == "donate":
        print("You choose "+Color.CYAN+"'donate'")
        money -= num_check("input amount to donate: ")

    print()
    if money <= 0:
        days = 0
    else:
        days -= 1

if money == 0:
    print(Color.BLUE + "You have spent all $1000000000.")
    print("You managed to spend all your money before you died, congratulations.")
    print("You feel fulfilled with your life before you pass.")
else:
    print(Color.RED + "You have spent $" + str(1000000000-money) + ".")
    print("You have died before you could spend all your money.")

