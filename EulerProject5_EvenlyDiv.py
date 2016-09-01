# This was a Challenage.. solved using largestprime function
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from EulerProject_HanFunctions import largestprime

total= 20
solution = 1

for x in range(1, total+1):
    if (solution%x!=0):
        solution=solution*largestprime(x)   #Multiply its largest prime number. Ths takes care of cases where x is either a prime or a power of a prime
    print x, solution



