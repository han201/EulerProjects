
#Find the sum of the digits in the number 100!




from EulerProject_HanFunctions import factorial
from EulerProject_HanFunctions import digits

#1.I used a brute-force method, and Python worked fine!
for N in range(1, 101):   # 100 inclusive
    X=factorial(N)
    print N, "!=", X, sum(digits(X, 10))

# To save some calculation, I could have excluded any number that is a multiple of 5 (5, 10, 15, 25, ...100).
# However, for 25, exclude 4 as well
# Elif,for a multiple of 5 that is not a multiple of 10, exclude 2 each time.
# I am not sure whether this will reduce the computation drastically or not.

