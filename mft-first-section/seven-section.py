from random import randint
secret = randint(0, 10)
print(secret)
while True:
    number = int(input("enter your number"))
    if number > secret:
        print("adad kochiktar vared kon")
    elif number < secret:
        print("adad bozorgtar vared kon")
    else:
        print("you win")
        break
    print("try again")
