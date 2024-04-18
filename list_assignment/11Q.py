l1=[]
for i in range(6):
    num=int(input('enter the numbners of list:'))
    l1.append(num)
print('elements \t  frequency')
for i in l1:
    print(i,end='\t \t \t \t')
    print(l1.count(i))