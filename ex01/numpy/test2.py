import numpy.random
import  numpy as np

names = np.array(['bob','asd','sailong','yake'])
print(names)
data = np.random.randn(7,4)
print(data)
data[data < 0] = 0
print(data)
#print(data)
print(names == 'bob')
