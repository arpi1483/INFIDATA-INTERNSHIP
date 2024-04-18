name=input('enter the name:')
cid=int(input('enter the cid:'))
print('the name is:',name)
print('the cid is:',cid)
e_bill=int(input())
if(e_bill<=100):
    print('no charge')
elif(e_bill>=100 and e_bill<=200):
    res=e_bill*5
    print('the bill amount is:',res)
elif(e_bill>200):
    res=e_bill*10
    print('the bill amount is:',res)