# it is use as a loop where list and loops of python is sloweer then numpy methods 

import numpy as np

arr = np.array([100,200,300])

discount = 10

finel_prices = arr - (arr * discount/100)

print(finel_prices)

# as the code as array u can directly apply loop or conditions and its called broad casting

#  its have some rools to working in array

# matching dimention if two arrays have same dimention then the broadcasting works normaly

# expanding single array elements

# if array has loop with single element then it expend array and make sure to initialise all elements with loop

# incompactible shapes if shape doesent match of two arrays numpy not expand that 


arr =np.array([1,2,3,4])

array = arr * 2     #single digit broadcasting with 1d

print(array)



arr = np.array([[1,2,3,4],[5,6,7,8]])
vector = np.array([10,20,30,40])        #1d array

result = arr + vector
print(result)