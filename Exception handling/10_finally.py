l1=[6,7,8,9]
print('list l1 is:',l1)
try:
    print('l1[2]:',l1[2])
    print('l1[5]:',l1[5])
except IndexError as e:
    print("am at IndexError except block,e valueis:,e")
except ZeroDivisionError as e:
    print("am at ZeroDivisionError except block")
    print('e value:', e)
finally:
    print('am at finally block:')
    print('executig at finally')
print('end')