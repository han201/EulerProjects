'''
Longest Collatz sequence: Which starting number, under one million, produces the longest chain?
https://projecteuler.net/problem=14
'''

from EulerProject_HanFunctions import collatz

maxlen=1     #Number of chains
maxcoll=1    #the collatz number that generates the maximum chain
for N in range(1, 10**6):
    len=collatz(N)
    if len > maxlen:
        maxlen=len
        maxcoll=N
        print maxcoll, " generates the maximum collatz chain length of ", maxlen

