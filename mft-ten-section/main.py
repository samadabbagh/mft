import re
f = open('majur')
text = f.read()
f.close()

pattern = r"O\s+(.+?)![\.,]?\s+[EXALTED].*O|s+(.+?![\.,]\s+KEEP"

result = re.findall(pattern, text)
print(result)