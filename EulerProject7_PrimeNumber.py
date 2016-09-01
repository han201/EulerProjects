# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from EulerProject_HanFunctions import isprime

# If prime number, factorize(N) == N

naturalnumber =2
nth = 0
NthPrime = 10001
while (nth < NthPrime):
    if (isprime(naturalnumber)):  # We found a prime number
        nth = nth + 1
        # if (nth==NthPrime):
        print nth, "th prime number is ", naturalnumber
    naturalnumber =naturalnumber+1
    if naturalnumber%2==0:                           # reduces the calculation by 20 sec. WIthout this, the run time is 70 sec.
        naturalnumber = naturalnumber+1
    elif (naturalnumber%3==0 and naturalnumber >3):   # adding additional filter did not reduce the runtime. Still took 50 sec.
        naturalnumber = naturalnumber + 1






