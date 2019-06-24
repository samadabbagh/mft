from random import randint
secret = randint(0, 10)
print(secret)
while True:
    number = int(input("enter your number"))
    if number > secret:
        print("enter smaller number")
    elif number < secret:
        print("enter bigger number")
    else:
        print("you win")
        break

