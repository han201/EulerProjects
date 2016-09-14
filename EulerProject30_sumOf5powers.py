
# Find the sum of all the numbers that can be written as the sum of 5th power of their digits

from EulerProject_HanFunctions import digits

#Find teh maximum such numbers.
maxdigit = 9**5 #9 power 5 is the maximum, which is 5 figure number
digit = 1
while (digit*maxdigit > 10**digit):
    digit=digit+1
#print digit
maxim = 7**5*digit     # maximum possible number
summ =0
print maxim
for candidate in range(2, maxim):
    digitlist = digits(candidate, 10)
    x=0
    digitsum=0
    for i in digitlist:
        digitsum = digitsum+i**5
    if digitsum == candidate:
        print digitsum, "is one such a number"
        summ = summ + candidate
print "The sum of all these numbers is", summ






