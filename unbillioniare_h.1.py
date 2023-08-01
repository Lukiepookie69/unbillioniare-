import random

money = 1000000000

gambleQ = input("Gamble? ")

if gambleQ == "yes":
    while money >= 0:
        print()
        amount = input("Select amount: (you have: "+str(money)+")")

        if amount == "all": amount = money

        amount = int(amount) * random.randint(-5, 7)

        money = money + int(amount)

        print()
        if int(amount) > 0: print("you earned $"+str(amount)+", giving you a total of $"+str(money))
        elif int(amount) < 0: print("you lost -$"+str(abs(amount))+", giving you a total of $"+str(money))
    
    print()
    print("You've lost too much money")