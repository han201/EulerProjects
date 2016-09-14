# Find the product of a and b where |a| < 1000, |b| < 1000 and n^2 + a * n + b has the maximum number of primes for a consecutive n >=0
# example: n^2 + n + 41 has 40 consecutive primes, and n^2 -79+1601 has 80 consecutive primes

from EulerProject_HanFunctions import isprime
'''
# first test the claim
j, k = 0,0
for n in range(0, 100):
    x = n**2 + n + 41
    if isprime(x)==1:
        print n, ":", x, " is a prime"
        j=j+1
    else:
        break
print j, " conseutive primes exist"

for n in range(0, 100):
    y = n ** 2 - 79 * n + 1601
    if isprime(y) == 1:
        print n, ":", y, " is a prime"
        k = k + 1
    else:
        break
print k, " conseutive primes exist"
'''


# test for a and b
maxn=0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n=0                       # initial n
        z = n ** 2 + a*n + b      # the number that we test
        while (z>0 and isprime(z)==1):
            n = n+1               # check for the next number
            z = n ** 2 + a * n + b  # the number that we test
        if n >maxn:
            print "a=", a, "and b=", b, "has product", a*b, "with", n, "consecutive primes"
            maxn =n





