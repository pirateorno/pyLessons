r = range(0, 10)
it = iter(r)

l = [1+5*(next(it)) for i in r]
print(l)