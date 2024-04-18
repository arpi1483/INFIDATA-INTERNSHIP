import  numpy as np

a1=np.array([1,2,3,4,5,6])
#add 1 to every element
print("adding 1 to every element: ",a1+1)

#substract 2 from each element
print("substract 2 from ecah element:",a1-2)

#multiplying each element by 10
print("multiplying each element by 10:",a1*10)

#square each element
print("squaring each element:",a1**2)

#modify existing array
a1 *=2  #a1=a1*2
print("double ecah element of original array:",a1)

#tanspose of array
a2=np.array([[1,2,3],[3,4,5],[9,6,0]])

print("\n original array:\n",a2)
print("transpose of array:\n",a2.T)