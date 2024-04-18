import numpy as np

#create an array from list with type float
a1=np.array([[1,2,3],[4,5,6]],dtype='float')#creating  an array with all float numbers
print('array contents are:',a1)#displaying the created array

#create array from tuple
a2=np.array((1,2,3))#creating array from tuples
print("array created from tuple is:",a2)#displaying the created arraay

#Creating a 16*173 array with all zeros
a3 = np.zeros((16,173))
print("\nAn array initialized with all zeros:\n", a3)

#creating a 17*17 array with all ones
one = np.ones((17*17))
print("\n An array initialised with all ones:\n",one)

#creating a matrix full of one number
a4 = np.full((17*17), -24.6728)#order = 17*17,required number= -24.6728
print("\n An array initialised with all 4.78654:\n",a4)

#create an array with random values
a5 = np.random.random((3,2))
print("\n A random array:\n",a5)

#Creating a sequence of integers from 0 to 49 with step of 5
a6 = np.arange(0,40,5)#start value is displayed, end value is
print("\n A sequential array with steps of 5:\n",a6)


#Creating a sequence of 10 values in range 0 to 40
a7 = np.linspace(0,40,10)#both starting and end point is displayed in result
print("\n A sequential array with 10 values  between 0 and 5:\n", a7)

#Flattern array
all= np.array([[1,2,3],[4,5,6]])
reshaped_array = all.reshape((1,-1))
reshaped_array_2=all.reshape((-1,1))

print("\n Originl array:\n",all)
print("Reshaped array:\n",reshaped_array)
print("Reshaped array:\n",reshaped_array_2)





