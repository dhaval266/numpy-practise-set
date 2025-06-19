import numpy as np

#to change array's dimention without modifying data of array use reshaping

array = np.array([1,2,3,4,5,6,7,8])

#reshape(raw,column) as parameters

reshape = array.reshape(2,4)        #it returns as view not copy 
print(reshape)


#for converting multidimentionle array to 1d array
#flatten()-> copy
#ravel()->view

array = np.array([[1,2,3,4],[5,6,7,8]])
print(array.ravel())
print(array.flatten())



