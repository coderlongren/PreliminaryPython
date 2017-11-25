from numpy import *
import  json
from scipy import *
def f(x):
    return  x*2
def add (x,y,f):
    return  f(x) + f(y)

print(add(1,2,f))
