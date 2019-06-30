from  price import data

#
# def fun(a):
#     return a[2] - a[1]
#
# f = lambda a: a[2] - a[1]

out = sorted(data, key=lambda a: a[2] - a[1], reverse=True)

print(data)
print(out)
mx = out[0]

print(mx)

indx  = data.index(mx)
print(data[indx])