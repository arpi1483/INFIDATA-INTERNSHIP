#for analysing and multiplying the array object
# munpy offer many ways to do array indexing:Slicing
import numpy as np

a1=np.array([[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]])
print("Array contents are \n",a1)

#slicing array1
s1=a1[:2,:3]
print("array with first 2 rows and first 3 columns:\n",s1)

#slicing array2
s2=a1[:2,::2]
print("array with first 2 rows and alternate columns:\n",s2)




























