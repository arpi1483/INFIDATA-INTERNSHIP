n1=int(input('enter the first number:'))
n2=int(input('enter the second number:'))
try:
    div=n1/n2
    print('result of div:',div)
except ZeroDivisionError as e:
    print('you are trying to divide a integer value by zero')
    print('e value is:',e)
print('end')