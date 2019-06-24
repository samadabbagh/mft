import random

fw = open('test1.txt', mode='w')

s = str(random.randint(1, 100))
fw.write(s)

print(s)