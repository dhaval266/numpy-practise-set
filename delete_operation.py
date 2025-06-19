import numpy as np

# as same as add , the delete method also create a new array 
#  to delete an array element we can use np.delete(array,index,axis=none)

arr = np.array([1,2,3,4,5,6])
print(arr)

new_arr = np.delete(arr,2,axis=None)
print(new_arr)


# for 2d array

arr = np.array([[1,2],[3,4]])
print(arr)

new_arr = np.delete(arr,0,axis=0)
print(new_arr)