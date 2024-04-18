try:
    A=9.999999999/5
except(ArithmeticError,IOError)as e:
    print(e)
else:
    print(A)