from _functools import reduce
def f(x):
    return x*x
def add (x,y):
    return  x+ y
r = map(f,[1,2,3,4,5,6])

print(r)
for x in r:
    print(x)
reduce(add,[1,2,3,4,5,6,7,8,9])
