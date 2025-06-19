import numpy as np 

# shape method use for information of array's shape

array_2d = np.array([[1,2,3,4],[5,6,7,8]])
print(array_2d.shape)   #(2,4) where tupple define as 2 raws and 3 columns

# for information of size that how many elements inn array

array_size = np.array([[1,2,3],[4,5,6]])
print(array_size.size)

# for information of how many dimention in array use ndim method

array_1d = np.array([1,2,3,4,5,6])
array_2d = np.array([[1,2,3],[4,5,6]])
array_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array_1d.ndim)
print(array_2d.ndim)
print(array_3d.ndim)

# for information of datatypes in array use dtype method 

array_type = np.array([1,2,3.5,4,4.5,6])
print(array_type.dtype) #mention that array only supports same datatype 

#for converting in new datatype use astype method

array_type = np.array([1,2.5,3,4,5.6,6])
arr_type = array_type.astype('i')
print(arr_type.dtype)

