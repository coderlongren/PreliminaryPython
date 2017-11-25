from scipy.optimize import fsolve # 求解方程组的函数
def f(x): # 定义要求解的方程组
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2 - 1,x1**2 - x2  - 2]

result = fsolve(f,[1,1])
print(result)