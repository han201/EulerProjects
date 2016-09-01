#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

# If a**2 + b**2 = c**2, then we found the solution.
refnum = 1000
for a in range(1, refnum):
    for b in range(1, refnum):
        d2=a**2 + b**2
        c = refnum - a - b
        if (c>0 and d2 ==c**2):
               print a, b, c, a*b*c
