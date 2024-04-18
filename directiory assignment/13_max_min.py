sub = {'maths': 80, 'java': 96, 'python': 95}

# taking list of values
l = list(sub.values())

# taking list of keys
k = list(sub.keys())

print(k[l.index(max(l))])