#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

from EulerProject_HanFunctions import isprime

naturalnumber =2
primesum = 0
maxprime = 2*10**6
while (naturalnumber < maxprime):
    if (isprime(naturalnumber)):  # We found a prime number
        primesum = primesum + naturalnumber
    if ((naturalnumber % 2 == 1) or (naturalnumber % 3 == 2 and naturalnumber > 3)):  # If the next number is a multiple of 3, skip to the next number
        naturalnumber = naturalnumber + 2
    else:
        naturalnumber = naturalnumber + 1

print "Sum of the prime numbers less than ", maxprime, " is ", primesum

'''
C:\Users\hahna\Anaconda2\python.exe C:/Users/hahna/PycharmProjects/EulerProjects/EulerProject10_PrimeSum.py
Sum of the prime numbers less than  2000000  is  142913828922

Process finished with exit code 0
'''


