'''
Find the sum of all the positive integers which CANNOT be written as the sum of two abundant numbers.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n
12 is the smallest abundant number
'''

from EulerProject_HanFunctions import perfect, abundant, deficient

sum=0
for i in range(1, 24):
    sum=sum+i                  # 24 is the smallest number that is the sume of two abundant numbers.

n=28123
#n=100
for i in range(24, n):    # identify i that is NOT a sum of two abundant numbers.
    j=2
    k=0
    while (j < i and k==0 ):
        if abundant(j)==1 and abundant(i-j)==1:    # i is a sum of two abundant number
            k=1
        else:
            j=j+1
    if k==0:              # we found a number that cannot be the sum of two abundant number
        sum=sum+i
        print i, "is Not a sum of two abundant numbers, so that the sum becomes", sum



