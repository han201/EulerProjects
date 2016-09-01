'''
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Solve for 2 number cases 0, 1
1: 01  ( 1 = 0*1!)
2: 10 ( 2 = 2* 1!. Reduce 2 by 1.


Solve for 3 number cases (0, 1, 2)
1: 012 (1 = 0*2! + 1. 1 = 0*1! + 1 so that we have 011. Since 1 showed up already , 1 becomes 2, so that we have 012)
2: 021 (2 = 0*2! +2 so that there will be a remainder. 2=2*1!. The remaining number becomes 1.
3: 102 (3 = 1*2! +1. 1 = 0*1! + 1, so that we have 101. but since 1 and 0 already showed up, 1 becomes 2.)
4: 120 (4 = 2*2! + 0. remainder 0 means that this is the biggest number 'BEFORE' the first digit 2.)
5: 201 (5 = 2*2!+1. 1=0*1! + 1 so that there is a remainder. 201)
6: 210 (6 = 3*2!. If there is no remainder, reduce by 1 so that we will have a remainder. 6 = 2*2! + 2. Next divide 2 by 1! so that it will have a remainder.
so that 2= 1*1! + 1. So we have 211. Since 1 already showed up, it becomes 0?)


Solve for 4 number cases (0, 1, 2, 3)
1: 0123
2: 0132
3: 0213
4: 0231
5: 0312
6: 0321   (6 = 1*3!. Since remainder is 0, it is the biggest number 03)
7: 1023   (7 = 1*3! + 0*2! + 1*1!. The last 1 becomes 2)
8: 1032  (8 = 1*3! + 1*2! +0. If the same number shows up and remainder is 0, it becomes one number smaller)
9: 1203  (9 = 1*3! + 1*2! + 1+1!, but 1 cannot be repeated. if the same number shows up, it will become 1 number bigger, so that the first 1 becomes 2, the second 1 becomes 3)
10: 1230 (10 =1* 3! + 2*2!. If the remainder is 0, it is the biggest number starting with 12. So 1230)
11: 1302 (11 = 1*3! + 2*2! + 1. The smallest number after 12XX, so that it is 1302)
12: 1320
13: 2013
14: 2031
15: 2103
16: 2130
17: 2301
18: 2310
19: 3012
20: 3021
21: 3102
22: 3120
23: 3201
24: 3210

'''

from EulerProject_HanFunctions import factorial

i=1
N=10**6
arr=[]
for i in range(1, 11):
    arr.append(factorial(i))
print arr


d =[]
e = []
for j in range(1, 9):
    d.append(N/arr[9-j])
    e.append(N%arr[9-j])
    print d, e
    N=N-d[j-1]*arr[9-j]

# using 2, 6, 6, 2, 5, 1, 2, 2 as the coefficient, we can construct 1M back.
print 2*factorial(9)+6*factorial(8)+6*factorial(7)+2*factorial(6)+5*factorial(5)+1*factorial(4)+2*factorial(3)+2*factorial(2)
'''
Construct the number based on the coefficient:
2 -> 2 (0, 1)
6 -> 7 (among 0 and 6, one number was used previously)
6 -> 8 (among 0 and 7, two numbers were used previously)
2 -> 3 (among 0 and 2, one number was used previously)
5 -> 9 (among 0 and 8, 4 numbers were used previously)
At this moment, the problem becomes a permutation problem with 5 numbers 0, 1, 4, 5, 6
1 -> 1 (should be bigger than a number starting with 0 to embrace 4!)
At this moment, the problme becomes a permutation problme with 3 numbers 0, 4, 5, and 6
2 -> 5 (should be bigger than a number starting with 0 and 4)
2 -> 4
the last one should be 60 (06 and 60 are two choices, but to embrace 2!, we need 60)
Therefore, we get 2783915460



'''

