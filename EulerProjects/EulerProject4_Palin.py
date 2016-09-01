#Challenge
#Find the largest palindrome which is a multiple of two 3 digit integers

zmax = 0  #initial palindrome
a=100
b=1000
for x in range (a, b):
    for y in range(a, b):
       z = x*y
# How do we check whether z is a palindrome or not?
# the minimum z is 10,000, while the maximum is 999,999. So we need to extract the integers
       digit1 = z%10
       digit2 = (z/10)%10
       digit3 = (z/100)%10
       digit4 = (z/1000)%10
       digit5 = (z/10000)%10
       digit6 = (z/100000)%10

       # print digit1, digit2, digit3, digit4, digit5, digit6

       if (digit6==0 and digit1==digit5 and digit2==digit4):
           if (z > zmax):
                 zmax=z
                 print "5 digit palindrome: ", x, "*", y, "=", z  # z is palindrome
       elif (digit6 != 0 and digit1 == digit6 and digit2 == digit5 and digit3 == digit4):
           if (z > zmax):
                 zmax=z
                 print "6 digit palindrome: ", x, "*", y, "=", z  # z is palindrome
print "maximum palindrome is ", zmax

