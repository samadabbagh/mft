number = int(input("enter your number number"))

i = 0
number_final = 0
while i < number :
    i = i+1
    number_final = number_final +(1 /i**2)

print(number_final)
pi =( 6 * number_final)**0.5


print(pi)