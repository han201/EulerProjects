#Find the largest palindrome which is a multiple of two 3 digit integers
from EulerProject_HanFunctions import digits

zmax = 0  #initial palindrome
a=100     # Given 3 digit integer is between a and b
b=1000
for x in range (a, b):
    for y in range(a, b):
       z = x*y           #a multiple of two 3 digit integers
# How do we check whether z is a palindrome or not?
# the minimum z is 10,000, while the maximum is 999,999. So we need to extract the integers with digit 5 or 6
       digit = digits(z, 10)   # returns array digit which stores each digit of N

       if (z < a*b):           # 5 digit palindrome. Probably does not contain a maximum, since there will be a palindrome with 6 digits
           if (digit[0]==digit[4] and digit[1]==digit[3]):
               if (z > zmax):
                   zmax=z
                   print "5 digit palindrome: ", x, "*", y, "=", z  # z is palindrome
       else:                    #6 digit palindrome. The maximum is likely in here
           if (digit[0] == digit[5] and digit[1] == digit[4] and digit[2] == digit[3]):
               if (z > zmax):
                   zmax=z
                   print "6 digit palindrome: ", x, "*", y, "=", z  # z is palindrome
print "maximum palindrome is ", zmax
