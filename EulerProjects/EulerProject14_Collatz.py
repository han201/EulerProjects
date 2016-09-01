'''
Longest Collatz sequence: Which starting number, under one million, produces the longest chain?
https://projecteuler.net/problem=14
'''

#First define collatz funtion, that calculates the chain
def collatz(coll):
    chain=1
    while coll > 1:
        if coll%2 ==0:
            coll=coll/2
        else:
            coll=3*coll + 1
        chain +=1
    return chain

maxlen=1     #Number of chains
maxcoll=1    #the collatz number that generates the maximum chain
for N in range(1, 1000000):
    len=collatz(N)
    if len > maxlen:
        maxlen=len
        maxcoll=N
        print maxcoll, " generates the maximum collatz chain length of ", maxlen

