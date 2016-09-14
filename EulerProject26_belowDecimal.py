
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

'''

(Theoretic Method)
1. construct an array arr with 1/1, 1/2, ... 1/999 (size 999)
2. Using round(arr[i], 2000), truncated up to 2000th digit.
3. using while loop, calculate j*arr - arr and only examine the below decimals:
# number_dec = str(number-int(number))[1:]

(Practical Method)

1. For d = 1 to 999, we want to calculate 1/d
2. remainders = {}
3. For each calculation, we want to do:
 initial value: a0 = 1, count = 1,
 a = a0*roundup[(d)]      # I need to round up d to the nearest multiple of 10's
 m = a%d
 if m belongs to any element of remainders, stop
 if m is different with any of the previous remainder, then count=count+1, a = m*10
 => I need a function that keeps track of all the remainders and see how to identify them.
4. Repeat step 3
 countarray.append(count)
5. Find maximum element of countarray.

Alternative of 4:
 maxcount = 1
 if count >= maxcount, maxcount = count. print d and maxcount
 '''

maxcount = 0
for d in range(1, 1000):
    remainder0 = 1
    remainders = [remainder0]  # initial remainder
    count = 1
    newNum = remainder0*10
    remainder = newNum%d
    while (remainder !=0 and (remainder not in remainders)):
        count = count+1
        remainders.append(remainder)
        newNum = remainder
        while (d > newNum):
            newNum = newNum*10
        remainder = newNum % d
    #print d, remainders, count
    if maxcount < count:
        maxcount = count
        print "1 over", d, "has", count, "repeating remainders"






