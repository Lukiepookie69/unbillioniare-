import random

money = 1000000000

gambleQ = input("Gamble? ")

if gambleQ == "yes":
    while money >= 0:
        print()

        game = random.randint(1, 3)

        if game == 1:
            print("Sports Gambling")
            print("There is a money limit of $100,000")
            print()

            amount = 100001 #temporary amount
            while int(amount) > 100000:
                amount = input("Select amount: (you have: "+str(money)+")")
                if amount == "all": 
                    if money < 100000: amount = money
                    else: amount = 100000

                if int(amount) > 100000: print("You can't place a bet higher than $100,000")

                if int(amount) <= 0:
                    print("invalid amount of money")
                    amount = 100001

            amount = int(amount) * random.randint(-5, 7)

            money = money + int(amount)

        elif game == 2:
            print("Illegal Dog fighting")
            print("There is no money limit")
            print()
            amount = input("Select amount: (you have: "+str(money)+")")
            if amount == "all": amount = money

            amount = int(amount) * random.randint(-5, 7)

            money = money + int(amount)
        
        elif game == 3:
            print("Lotto")
            print("Each ticket costs $1, the cash prize for winning is $250 Million")    #250000000
            print("There is no limit to how many tickets you can buy")
            print()
            amount = input("Select amount: (you have: "+str(money)+")")
            if amount == "all": amount = money

            if random.random() < int(amount)/100000000: #one in 100000000 chance(i think thats how the math works?)
                print("you won")
                amount = 250000000
            else:
                print("you lost")
                amount = int(amount) * -1

            money = money + int(amount)


        print()
        if int(amount) > 0: print("you earned $"+str(amount)+", giving you a total of $"+str(money))
        elif int(amount) < 0: print("you lost -$"+str(abs(amount))+", giving you a total of $"+str(money))
    
    print()
    print("You've lost too much money")