#comparison between time required to add two lists and two numpy arrays

"""list addition"""
import numpy as np
import time
numpy_array1 = np.random.randint(0,100,size=1000000)#creating array of size 10000 of random integers between 0 and 100(exclusive)"""
numpy_array2 = np.random.randint(0,100,size=1000000)#same

list1 = list(numpy_array1)
list2 = list(numpy_array2)#converting numpy array into list

start_time = time.time()
for _ in range(1000):
    list_sum = [(a+b for a,b in zip(list1,list2))]
end_time= time.time()
print("list time required=", end_time-start_time)
t3 = time.time()
for _ in range(1000):
    numpy_sum = numpy_array1+numpy_array2

t4= time.time()
print("numpy time required=", t4-t3)
