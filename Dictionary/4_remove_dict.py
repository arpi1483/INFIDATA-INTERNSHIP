d1={1:1,2:4,3:9,4:16,5:25,6:36}
print(d1)

print('pop value is:',d1.pop(2))
print('new dictionary is:',d1)

print('pop value is:',d1.popitem())
print('updated dictionary is:',d1)

print('clear dictionary is:',d1.clear())
print('updated dictionary is:',d1)

del d1                                 #delete the dictionary
print('deleting dictionary is:',d1)    #name error