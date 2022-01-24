
#ATM with interactive menu

from random import randrange

balance = randrange(0,5000000)

print("*** Welcome to the Cash Machine ***")
while True:
    print("\nAvailable operations")
    print("\n1. Balance")
    print("2. Withdrawal of money")
    print("3. Deposit")
    print("0. Exit")

    option = int(input("Choose the operation to be performed between 0 - 3: "))
    if option in range(4):
        if option == 1:
            print("Your balance is: ", balance)
        elif option == 2:
            amount = int(input("Indicate the amount to be withdrawn: "))
            if amount > balance:
                print("Invalid operation, insuffcient balance")
            else:
                balance = balance - amount
                print("Sucessful operation")
                print("Your current balance is: ", balance)
        elif option == 3:
            amount = int(input("Indicate the amount to deposit"))
            balance = balance + amount
            print("Your current balance is: ", balance)
        else:
            print("See you soon..")
            break
    else:
        print("The select option is not avaible")
