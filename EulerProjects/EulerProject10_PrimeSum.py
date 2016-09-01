#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

# This function finds the biggest factor of N. We will use this to identify a power of a single number or a prime number

def factorize(N):
    factor = 2
    while (factor <= N):
         if N%factor==0:
              N=N/factor

    else:
    factor = factor + 1


return factor
# If prime number, factorize(N) == N

naturalnumber =2
primesum = 0
maxprime = 2000000
while (naturalnumber < maxprime):
    if (factorize(naturalnumber)== naturalnumber):  # We found a prime number
        primesum = primesum + naturalnumber
    naturalnumber =naturalnumber+1
print "Sum of the prime numbers less than ", maxprime, " is ", primesum

'''
C:\Users\hahna\Anaconda2\python.exe C:/Users/hahna/PycharmProjects/EulerProjects/EulerProject10_PrimeSum.py
Sum of the prime numbers less than  2000000  is  142913828922

Process finished with exit code 0
'''


