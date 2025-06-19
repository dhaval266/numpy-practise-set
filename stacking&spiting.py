# for stacking in raw or column wise we have two methods 

# vstack = to stack row wise or verticaly
# hstack = to stack column wise or horizontly

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1,arr2)))   #verticaly stack
print(np.hstack((arr1,arr2)))   #horizontaly stack



# for spliting there is three methods

# for equal spliting we have np.split(array,number)  where number represent the part of spliting array in
# for verticaly split we have np.vsplit()
# for horizontly spit we have np.hsplit()

arr = np.array([1,2,3,4,5,6])

print(np.split(arr,2))

print(np.hsplit(arr,2))

arr = np.array([[1,2,3],[4,5,6]])
print(np.vsplit(arr,2))
