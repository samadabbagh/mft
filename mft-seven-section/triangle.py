import random

fw = open('inp.txt', mode='w')
triangle_count = 0
triangle_same = 0
triangle_saghein = 0
triangle_ghaem = 0
for i in range(1000):
    max1 = 0
    numbers = []
    for j in range(3):
        s = random.randint(1, 20)
        fw.write(str(s))
        fw.write(',')
        if s > max1:
            max1 = s
            numbers.insert(0, s)
        else:
            numbers.append(s)
    if numbers[1]+numbers[2] > numbers[0]:

        triangle_count += 1

        if numbers[0] == numbers[1] == numbers[2]:
            triangle_same += 1
        else:
            if numbers[1] == numbers[0] or numbers[0] == numbers[2] or numbers[1] == numbers[2] :
                 triangle_saghein += 1
            if numbers[1]**2 + numbers[2]**2 == numbers[0]**2:

                triangle_ghaem += 1

    fw.write('\n')
fw.close()
print("count of triangle:", triangle_count)

print("mosalas motesaviol azla:", triangle_same)
print("mosalas motesaviol ghaem:", triangle_ghaem)
print("mosalas motesaviol saghein:", triangle_saghein)