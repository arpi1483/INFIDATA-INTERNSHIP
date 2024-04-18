l1=[2,3,4,5,6]
print('list l1 is:',l1)
try:
    print('l1[2]:',l1[2])
    print('l1[5]:',l1[5])
    print('l1[4]:',l1[4])
except IndexError as e:
    print('u r trying to access wrong index')
    print('e value is:',e)
print('end')
