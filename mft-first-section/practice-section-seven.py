fr = open('tree.txt')

tree = fr.read()
num, pattern = tree.split('\n')
num = int(num)
fr.close()

line = pattern * num + '\n'
s = line * num

fw = open('tree-output.txt', mode='w')

fw.write(s)
fw.close()


