l1=[2,3,4,10,15,16,4,50]
print('list l1 is:',l1)

l1.pop()
print('updated l1 is:',l1)

l1.pop(4)
print('updated l1 is:',l1)

l1.pop(8)#if no position present it provides index error
print('updated l1 is:',l1)

l1.remove(10)
print('updated l1 is:',l1)

l1.remove(10)#if element not present it provides value error
print('updated l1 is:',l1)