print('function with return value demo')
def addition(a,b):
    sum=a+b
    return sum

print('addition pgm using function')
n1=int(input('enter first num'))
n2=int(input('enter second num'))
res=n1+n2
print('add of {0} and {1} is {2}'.format(n1,n2,res))
print('add of {0} and {1} is {2}'.format(n1,n2,addition(n1,n2)))
print('end of the code')