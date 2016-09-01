
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


from EulerProject_HanFunctions import fibo

N=10**(1000-1)         # The minimum number that contians 1000 digits
i=1
while (fibo(i)< N):
       i=i+1
print "The first fibonacci number that exceds N is index", i
