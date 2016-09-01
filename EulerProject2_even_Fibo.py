
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#1. Let's genearate Fibonacci numbers below 4,000,000

from EulerProject_HanFunctions import fibo

N = 4*10**6
i=1
sum=0
while (fibo(i) <= N):
    if (fibo(i)%2==0):
       sum = sum + fibo(i)
    i=i+1
print fibo(i), sum

