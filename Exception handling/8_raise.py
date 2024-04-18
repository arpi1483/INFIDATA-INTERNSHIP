print('raise keyword demo')
try:
    raise ZeroDivisionError("demo message")
except ZeroDivisionError as e:
    print('am at ZeroDivisionError except block')
    print('e value:',e)
print('end')