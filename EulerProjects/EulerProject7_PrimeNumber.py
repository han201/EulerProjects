# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# This function finds the biggest factor of N. We will use this to identify a power of a single number or a prime number

def factorize(N):
    factor = 2
    while (factor <= N):
         if N%factor==0:
              N=N/factor
         else:
              factor=factor+1
    return factor

# If prime number, factorize(N) == N

naturalnumber =2
nth = 0
NthPrime = 10001
while (nth < NthPrime):
    if (factorize(naturalnumber)== naturalnumber):  # We found a prime number
        nth = nth + 1
        # if (nth==NthPrime):
        print nth, "th prime number is ", naturalnumber
    naturalnumber =naturalnumber+1





