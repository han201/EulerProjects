'''
d(n) be the sum of proper divisors of n (divisors less than n itself)
if d(a) = b an d(b)=a (a !=b), then a and b are amicable.
For example, d(284) = 220
Find the sum of all the amicable numbers < 10,000
'''

from EulerProject_HanFunctions import sumDiv

sum=0
for i in range(2, 10000):
    if ( sumDiv(sumDiv(i)) == i ):
        if (sumDiv(i) !=i ):
            sum = sum+i
            print i, sumDiv(i), sumDiv(sumDiv(i)), sum
        else:
            print "The sum of proper divisors is the number itself : ", i
print sum
