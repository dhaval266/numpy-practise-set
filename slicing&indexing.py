import numpy as np

array_index = np.array([1,2,3,4,5,6,4,7])

# for 1d array can use array[index]

print(array_index[4])


# for 2d array use array[raw,index] or can use raw as dimention number

array = np.array([[1,2,3,4],[5,6,7,8]])
print(array[1,2])

#for 3d array use array[raw,raw,index] or can use raw as dimention number

array = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array[1,0,2])


#for slicing use array[start:stop:step] where start included but stop not and step is for jump

array = np.array([1,2,3,4,5,6,7,8,9])
print(array[1:3])   #mentioned start and stop only

print(array[1:6:2])     #mentioned start stop and step/jump

print(array[:6])        #mentioned only end that consider starting from array's first

print(array[2:])        #mentioned only start that consider ending of array

print(array[::3])       #mentioned only jump element that consider start to end of array with jump

print(array[::-1])      #negetive step slicing that revrsed the array 



# fancy selecting elements 

#have to pass a list of index to select eelememt of array

print(array[[1,5,6]])



#boolean masking / filtering 

#have to use condition as parameter in filtering


print(array[array < 6])