# you are a billionaire and have 10 days to spend all your money
# your name is John Bars, you do not have a wife, you repressed all your homosexuality

import pandas


# check that user enter a valid response
def string_checker(question, num_letters, valid_responses):

    error = "please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

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


money = 1000000000  # billion
days = 5
yes_no_list = ["yes", "no"]
buy_gam_don_list = ["buy", "gamble", "donate"]


print()
print(Color.RED + "UN-BILLIONAIRE" + Color.END)
print()


if string_checker(Color.GREEN + "Do you want to read the instructions? (y/n): ", 1, yes_no_list) == "yes":
    print(Color.BLUE + "Instructions go here")  # fill out instructions

print(Color.END)

while days > 0:
    if days == 1:
        print(Color.GREEN + "You have " + str(days) + " day to spend $" + str(money)+".")
    else:
        print(Color.GREEN + "You have " + str(days) + " days to spend $" + str(money)+".")

    print("Choose wisely")
    print()
    print("BUY")
    print("GAMBLE")
    print("DONATE")

    choice = input()
    days -= 1


