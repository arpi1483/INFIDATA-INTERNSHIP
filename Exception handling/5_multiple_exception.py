n1=int(input('enter the first number:'))
n2=int(input('enter the second number:'))
l1=[4,5,6,7,8]
print('list l1 is:',l1)
try:
    div=n1/n2
    print('res of div is:',div)
    print('l1[2]:',l1[2])
    print('l1[4]:',l1[4])
except ZeroDivisionError as e:
    print('u r trying to divide int by zero')
    print('e value is:',e)
except IndexError as e:
    print('u r trying to access wrong index')
    print('e value is :',e)
print('end')