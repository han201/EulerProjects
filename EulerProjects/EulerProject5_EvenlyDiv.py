#Challenge
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# This function finds the biggest factor of N. We will use this to identify a power of a single number or a prime number
def factorize(N):
    factor = 2
    while (factor <= N):
         if N%factor==0:
              N=N/factor
         else:
              factor=factor+1
    return factor


total= 20
solution = 1

for x in range(1, total+1):
    if (solution%x!=0):
        solution=solution*factorize(x)
    print x, solution



