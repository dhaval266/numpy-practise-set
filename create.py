import numpy as np


# for creating an array from list

l = [1,2,3,4,5,6]

array = np.array(l)
print(array)

# for creating an array as default values

array = np.zeros((2,3))  #in tupple has value of shap that define shape of array
print(array)

# for creating array as default values 1

array = np.ones((2,3))  # as default value is 1
print(array)

#  for create an array with full values 

array = np.full((2,3),5)    #first tupple for shape and second value for default value
print(array)

# to make an array with a range 

array = np.arange(2,200,4)  #where the parameters is ('start','stop','step')
print(array)

# to make identity matrix 

identity_array = np.eye(4)  #the parameter is shape where identity metrix is a squre matrics
print(identity_array)

