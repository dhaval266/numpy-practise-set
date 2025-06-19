import numpy as np

#to add or insert in array use np.insert(array,index,number,axis=none) paramete has the number where it can be anything according to datatype
#np.insert(arra,index,value,axis=none)
# array->originle array
# index->index number where to insert
# value->value that according to datatype
# axis->for 1d its flatten(), for 2d it has 0 for raw and 1 for column wise insertion axis=0 horizontal stack, axis=1 vertical stack
# add or insertion are generating new array 

# 1d array insertion
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)

new_arr = np.insert(arr,3,40,axis=0)
print(new_arr)

# 2d array insertion
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)

new_arr = np.insert(arr,1,[10,20,30,40],axis=0)
print(new_arr)



# to add value at the lst use np.append(array,value)

arr = np.array([1,2,3,4])
print(arr)

new_arr = np.append(arr,[5,6,7,8])
print(new_arr)



#to join or concatenate 2 or more array use np.concatenate((array1,array2),axis=none) where the parameter of the array is in a tuple

arr1 = np.array([[1,2,3,4]])
print(arr1)

arr2 = np.array([[5,6,7,8]])
print(arr2)

arr = np.concatenate((arr1,arr2),axis=0)
print(arr)

arr_v = np.concatenate((arr1,arr2),axis=1)
print(arr_v)