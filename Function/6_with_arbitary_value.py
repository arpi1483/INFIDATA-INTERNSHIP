print('function with arbitrary value')
def addition(*num):
    sum=num[0]+num[1]
    print('add of {0} and {1} is {2}'.format(num[0],num[1],sum))
print('addition pgm using function')
addition(10,40)
print('end of the code')