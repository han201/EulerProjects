#The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# What is the value of the first triangle number to have over five hundred divisors?
'''
1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
'''

#First let's find a function that calculates the number of divisors for an integer
def numDiv(N):
    numberDiv=1
    for factor in range(1, N):
        if N%factor==0:
                numberDiv +=1
    return numberDiv

#print numdiv(3), numdiv(6), numdiv(10), numdiv(15), numdiv(21), numdiv(28)

element=1
numberOfDiv=1
sumElement=1
while (numberOfDiv < 500):
    element +=1
    sumElement = sumElement + element
    numberOfDiv=numDiv(sumElement)
print element, sumElement, numberOfDiv


