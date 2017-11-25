def is_odd(n):
    return n%2 == 1
for x in (list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))):
    print(x)
s = " f "
print("s len is : %d"%len(s))
print(s.strip())
print(len('s len is :%d'%len(s)))