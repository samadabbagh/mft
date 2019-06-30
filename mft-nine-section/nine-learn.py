data = [(3, 9), (1, 10), (2, 4), (90, 91)]

out = sorted(data, key=lambda d: d[1] - d[0])

print(data)
print(out)