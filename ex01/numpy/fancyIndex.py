import  numpy as np

# arr = np.empty((8,4))
# for i in range(8):
#     arr[i] = i
# print(arr)

arr = np.arange(15).reshape((3,5))
print(arr)
#矩阵的  转置
arr1 = arr.T
print(arr1)
arrDot = np.dot(arr.T,arr)
print(arrDot)

