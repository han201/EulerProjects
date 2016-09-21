'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

from EulerProject_HanFunctions import digits

'''
# check to see whether there is a patern or not.
for i in range(1, 20):
    x=digits(2**i, 10)
    print i, x, sum(x)
# looks random, so let's go for the answer straight
'''
x = 2 ** 1000;
y = digits(x, 10)
print 1000,x, sum(y)