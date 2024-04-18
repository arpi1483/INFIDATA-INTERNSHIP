l1 = []
s = int(input('How many elements you want to enter '))

print('Enter',str(s),'positive numbers')

for i in range(s):
    data = int(input())
    l1.append(data)

max = 0
for data in l1:
    if data > max:
        max = data

print('The largest number in list is', max)