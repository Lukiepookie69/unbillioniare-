# you are a billionaire and have 10 days to spend all your money
# your name is John Bars, you do not have a wife, you repressed all your homosexuality

import random

money = 1000000000  # billion
days = 3
yes_no_list = ["yes", "no"]
buy_gam_don_list = ["buy", "gamble", "donate"]
buy_name_list = [
    "Expensive Yacht",
    "Dead Shark",
    "5.0 Carat Diamond",
    "1962 Ferrari",
    "Superhero Franchise Film Rights"
]
buy_price_list = [
    100000000,
    8000000,
    333000,
    160000000,
    4000000000
]
moneyspent = [
    0,
    0,
    0
]


# check that user enter a valid response
def string_checker(question, num_letters, valid_responses):

    if valid_responses == buy_gam_don_list:
        error = "please choose {}, {} or {}".format(valid_responses[0], valid_responses[1], valid_responses[2])
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
            response = input(question)
            if response == "all":
                return money
            if int(response) > 0:
                if int(response) <= money:
                    return int(response)
                else: print("You don't have that much money")
            else: print("You can't enter a negative number")


        except ValueError:
            print("Please enter an number value")

def comma_add(num):
    return '{:,}'.format(num)


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
    print(Color.BLUE + "You have 3 days to spend a billion dollars.")
    print("It's your goal to find a way to spend all billion dollars by either buying items, gambling, or donating")
    print()
    print("Typing 'all' while gambling or donating will spend all your money in your account")

print(Color.END)

while days > 0:
    if days == 1:
        print(Color.YELLOW + "You have " + str(days) + " day to spend $" + comma_add(money)+".")
    else:
        print(Color.YELLOW + "You have " + str(days) + " days to spend $" + comma_add(money)+".")

    print("Choose wisely")
    print()
    print(">BUY")
    if days == 3: print(">GAMBLE(LOTTO)")
    elif days == 2: print(">GAMBLE(ILLEGAL DOG FIGHTING)")
    elif days == 1: print(">GAMBLE(SPORTS GAMBLING)")
    print(">DONATE")

    choice = string_checker(Color.YELLOW + "Choose: ", 1, buy_gam_don_list)

    if choice == "buy":
        print("You choose "+Color.GREEN+"'buy'")
        # prints list of items to buy, select your choice by number
        for n in range(len(buy_name_list)):
            price = comma_add(buy_price_list[n])
            print("(Item " + str(n+1) + "): " + buy_name_list[n] + ": $" + price)

        item = num_check("Select item to buy (the number the item is listed under): ") - 1
        while item >= len(buy_name_list) + 2:
            item = num_check("Please select item to buy (the number the item is listed under): ") - 1
        while buy_price_list[item] > money:
            item = num_check("Please select an item in the price range (the number the item is listed under): ") - 1

        print("You bought a " + buy_name_list[item] + " for $" + str(buy_price_list[item]))
        moneyspent[0] += buy_price_list[item]
        money -= buy_price_list[item]

    elif choice == "gamble":
        print("You choose "+Color.PURPLE+"'gamble'")
        print()

        if days == 1:
            print("Sports Gambling.")
            print("There is a money limit of $100,000.")
            print()
        
            amount = 100001  # temporary amount
            while int(amount) > 100000:
                price = comma_add(money)
                amount = num_check("Select amount: (you have: "+price+") ")

                if int(amount) > 100000: print("You can't place a bet higher than $100,000")

                if int(amount) <= 0:
                    print("invalid amount of money")
                    amount = 100001
            
            amount = int(amount) * random.randint(-5, 7)
            moneyspent[1] += int(amount)
            money = money + int(amount)
        
        elif days == 2:
            print("Illegal Dog fighting.")
            print("There is no money limit.")
            print()
            price = comma_add(money)
            amount = num_check("Select amount: (you have: $"+price+") ")

            amount = int(amount) * random.randint(-5, 8)
            if amount < 0: moneyspent[1] -= int(amount)
            elif amount >= 0: moneyspent[1] += int(amount)
            money = money + int(amount)
        
        elif days == 3:
            print("Lotto.")
            print("Each ticket costs $1, the cash prize for winning is $250,000,000")
            print("There is no limit to how many tickets you can buy.")
            print()
            print(Color.BLUE+"Tip: its a one in ten million chance")
            print(Color.PURPLE)
            price = comma_add(money)
            amount = num_check("Select amount: (you have: "+price+") ")

            if random.random() < int(amount)/100000000:  # one in 100000000 chance(i think thats how the math works?)
                money -= amount
                print("you won $250,000,000!")
                money += 250000000
            else:
                print("you lost $" + str(amount))
                money -= amount

            moneyspent[1] += int(amount)

    elif choice == "donate":
        print("You choose "+Color.CYAN+"'donate'")
        amount = num_check("input amount to donate: ")
        money -= amount
        moneyspent[2] += amount

    print()
    if money <= 0:
        days = 0
    else:
        days -= 1

print(Color.GREEN+"Money spent:")
for n in range(len(buy_gam_don_list)):print(buy_gam_don_list[n-1]+": $"+comma_add(moneyspent[n-1]))
print()

if money <= 0:
    if moneyspent[2] >= moneyspent[1] and moneyspent[2] >= moneyspent[0]:
        print(Color.GREEN + "You have spent all $1,000,000,000 you had three days ago.")
        print("You spent most your money donating,")
        print("you feel fulfilled with your life before you pass.")
    elif moneyspent[1] >= moneyspent[2] and moneyspent[1] >= moneyspent[0]:
        print(Color.RED + "You have spent all $1,000,000,000 you had three days ago")
        print("you spent most of your money gambling,")
        print("You may not feel fulfilled on your death bed, but at least you felt a frill in your last days.")
    elif moneyspent[0] >= moneyspent[2] and moneyspent[0] >= moneyspent[1]:
        print(Color.RED + "You have spent all $1,000,000,000 you had three days ago")
        print("you spent most of your money buying things,")
        print("You do not feel good about your life on your death bed.")

else:
    print(Color.RED + "You have spent $" + comma_add(-money-1000000000) + ".")
    print("You have died before you could spend all your money.")



