T1=(10, 20, 30, 40, 50, 60)
num=int(input('enter the number:'))
t1_rem=list(T1)
if num in t1_rem:
    t1_rem.remove(num)
    print('number removed successfully')
    T1=tuple(t1_rem)
print('after deleting the element:',T1)

