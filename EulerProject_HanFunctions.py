
#largestprime functinon calculates the largest prime number of natural number N
def largestprime(N):
    factor = 2
    while (factor <= N):
         if N%factor==0:
              N=N/factor
         else:
             factor = factor + 1
    return factor

# Returns true if N is a prime number
def isprime2(N):
    if largestprime(N)==N:
        return 1
    else:
        return 0

        # returns true if N is a prime number: 2, 3, 5, 7, 11, 13, 17, etc


def isprime(N):
    primen = 0
    if N == 1:  # by definition
        primen = 0
    elif N == 2 or N == 3 or N == 5 or N == 7:  # initial for prime numbers
        primen = 1
    else:
        maxim = int(N ** 0.5)
        primen = 0
        j = 3
        while (N % 2 > 0 and N % 3 > 0 and j <= maxim):  # detect a prime. The default is Not a prime
            if N % j == 0:
                primen = 0
                break
            else:
                j = j + 2
                primen = 1
    return primen

# Calculates the number of divisors for an integer using a brute force method
def numDiv_bruteforce(N):
    numberDiv = 1
    for factor in range(1, N):
        if N % factor == 0:
            numberDiv += 1
    return numberDiv

# Calculates the number of divisors for an integer, with 50% less calculation than the brute-force method
def numDiv(N):
    numberDiv=2               # The mininum possible number of factors is 2: 1 and N
    for factor in range(2, N, 1):
        if (N%factor ==0):
            if (factor**2 <N):
                numberDiv +=2
            elif (factor**2 == N):
                numberDiv +=1
            else:
                break         # break out of the for loop
    return numberDiv

# Calculates the sum of all divisors
def sumDiv(N):
    sumDivisor=1               # The minimum possible number of factors is 2: 1 and N
    for factor in range(2, N, 1):
        if (N%factor ==0):
            if (factor**2 <N):
                sumDivisor = sumDivisor + factor + N / factor
            elif (factor**2 == N):
                sumDivisor = sumDivisor + factor
            else:
                break         # break out of the for loop
    return sumDivisor

#Checks for perfect, abundant and deficient numbers
def perfect(N):
    if sumDiv(N)==N:
        return 1
    else:
        return 0

def abundant(N):
    if sumDiv(N)>N:
        return 1
    else:
        return 0

def deficient(N):
    if sumDiv(N)<N:
        return 1
    else:
        return 0



#Returns true if N is a multiple of m
def multipleOf(N, m):
    if N%m ==0:
        return 1
    else:
        return 0

#digits function returns a list of each digits in numeric system. Look at the example
# print digits(12345, 10)
def digits(N, system):
    digit=list()
    while (N >0):
        digit.append(N%system)
        N=N/system
    return digit

#factorial
def factorial(N):
    fact=1
    for i in range(1, N+1):
        fact = fact*i
    return fact


#generates Nth fibonacci number
def fibo(N):
    fibo1 = 1
    fibo2 = 2
    fibo3 = 3
    if N==1 or N==2:
        return fibo1
    elif N==3:
        return fibo2
    elif N==4:
        return fibo3
    else:

        for i in range(5, N+1):
            fibo1=fibo2
            fibo2=fibo3
            fibo3 = fibo1 + fibo2
        return fibo3
