pay=int(input('enter the amount:'))
location=input('enter the place:')
if(location=='mumbai'):
    print('Ill take it!')
elif(location=='chennai'):
    if(pay<100000):
        print('no way')
    else:
        print('iam willing')
elif(location=='delhi' and pay>40000):
    print('iam happy to join')
elif(pay>60000):
    print('I accept the offer')
else:
    print('no thanks,i can find something better')
