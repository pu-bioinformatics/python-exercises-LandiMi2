#!/home/cofia/miniconda3/bin/python #CK: This shebang is specifci to your system

acountbal = 50000
choice = input("Please enter 'b' to check balance or 'w' to withdraw or deposit 'd': ")
while choice != 'q':
    if choice.lower() in ('w','b','d'):
        if choice.lower() == 'b':
            print("Your balance is: %d" % acountbal)
            print("Anything else?")
            choice = input("Enter b for balance, w to withdraw or q to quit: ")
            print(choice.lower())
        elif choice.lower() == 'd' :
                deposit = float(input("Enter amount to deposit:"))
                if deposit > 0:
                    print("This is the  amount you have deposited:%d" %deposit)
                    acountbal = acountbal + deposit
                    print("Anything else?")
                    choice = input("Enter b for balance, w to withdraw or q to quit: ")
        else:
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw <= acountbal:
                print("here is your: %.2f" % withdraw)
                acountbal = acountbal - withdraw
                print("Anything else?")
                choice = input("Enter b for balance, w to withdraw or q to quit: ")
                
            else:
                print("You have insufficient funds: %.2f" % acountbal)
    else:
        print("Wrong choice!")
        choice = input("Please enter 'b' to check balance or 'w' to withdraw: ")