# it is same as broadcasting where we not use loop for arrays

# as example
import numpy as np

arr1 =np.array([1,2,3])
arr2 = np.array([4,5,6])

result = arr1 + arr2
print(result)

result_mul = arr1 * arr2
print(result_mul)

# as broadcasting its expend smaller arrya to larger array and its faster then loops
# where vectorisation is applied operation to all array at a time and its 100x fatser then loops