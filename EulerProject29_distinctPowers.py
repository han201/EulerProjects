#calculating the number of elements in set

firstset = set()
z=101
for a in range(2, z):
    for b in range(2, z):
        x = a**b
        firstset.add(x)
sorted(firstset)
print len(firstset)

