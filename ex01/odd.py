#_*_coding: utf-8 _*_
def my_abs(x):
    if x > 0:
        return  x
    else :
        return -x
def _odd_iter():
    # 这是一个生成器，并且是一个无线序列
    n = 2
    while True:
        n = n + 2
        # yield 返回n
        yield  n
def _not_divisible(n):
    #这是一个筛选函数
    return  lambda x : x%n > 0
# 使用唉氏筛法
def primes():
    # 第一次返回2
    yield 2
    # 使用生成器  初始化序列
    it = _odd_iter()
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n),it)# 构造新序列


for n in primes():
    if (n < 1000):
        print(n)
    else:
        break


#print(my_abs(-5))