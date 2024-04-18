print('function return multiple value')
def arithmetic(n1,n2):
    sum=n1+n1
    mul=n1*n2
    return sum,mul
print('arithmetic operation using function')
n1=int(input('enter first num'))
n2=int(input('enter second num'))
res1,res2= arithmetic(n1,n2)
print('add of {0} and {1} is {2}'.format(n1, n2, res1))
print('mul of {0} and {1} is {2}'.format(n1,n2,res2))