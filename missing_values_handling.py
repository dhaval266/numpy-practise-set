# for the missing values we have some methods that use in case else it return error 

# np.isnan()  detect missing values
# np.nan_to_num()   to convert missing values in number
# np.isinf()    to detect missing values is infinite
# nan stand for not a number

import numpy as np

arr = np.array([1,2,np.nan,5,6,np.nan])
print(np.isnan(arr))

# mentione that u can not comapre nan values directly

# to replace nan value to number we use np.nan_to_num(arr,nan=value) default-0

cleaned_arr = np.nan_to_num(arr)
print(cleaned_arr)

cleaned_arr = np.nan_to_num(arr,nan=100)
print(cleaned_arr)



# to make inf value we use np.inf and for detect it we use np.isinf(array)

arrr = np.array([1,2,np.inf,5,6,-np.inf])
result = np.isinf(arrr)
print(result)


# to replace inf to number we also use np.nan_to_num(array , posinf=1000 , neginf=-1000)    where posinf for positive inf and neginf for negative inf
result = np.nan_to_num(arrr,posinf=1000,neginf=-1000)
print(result)