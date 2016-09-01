#What is the largest prime factor of the number 600851475143 ?

N = 600851475143
factor = 2
while (factor <= N):
    if N%factor==0:
       N=N/factor
       print factor
    else:
       factor=factor+1;
print factor

