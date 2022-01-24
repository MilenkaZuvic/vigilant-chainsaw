
#Playing guess de number

from random import randint

x = randint(1,25)

attempts = 0

#We need a repetitive structure to control the number of attempts

while attempts < 6:
    number = int(input("Choose a number between 1 y 25 "))
    attempts = attempts + 1
    if number > x:
        print("Your number is above")
    elif number < x:
        print("Your number is below")
    else:
        break

if number == x:
    print("Congratulations... You are a genius...")
    print("You did it in {} attempts".format(attempts))
else:
    print("uy... you lost, will be another time")
