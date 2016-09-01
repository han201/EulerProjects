'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
'''

from EulerProject_CountingInEnglish import countingNumbers
from EulerProject_CountingInEnglish import countingGeneral
print countingNumbers(0)


sum=0
for N in range(1, 1001):   # 1000 inclusive
    print N, " is pronounced ", countingGeneral(N), " with ", countingNumbers(N), " letters"
    sum=sum+countingNumbers(N)
print sum
