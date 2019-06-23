fr = open('text.txt')
text = fr.read()

num, pattern = text.split('\n')
num = int(num)
fr.close()
line = pattern * num + '\n'
s = line * num

fw = open('output.txt', mode='w')
fw.write(s)
fw.close()