d1={}
d2={}
for i in range(2):
    key=input("enter a key in string:")
    value=input("enter a value")
    d2={key:value}
    print(d2)
    d1.update(d2)
print(d1)
