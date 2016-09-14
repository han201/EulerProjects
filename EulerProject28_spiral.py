
# sum of the numbers on the diagonals in a 1001 by 1001 spiral
'''
(Examples)
size1: number 1
size2: 3*3 matrix with numbers 1, 2, 3, 4, 5, 6, 7, 8, 9 / new diagonals are 3, 5, 7, 9 (jump by 2)
size3: 5*5 matrix with numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 21, 22, 23, 24, 25
new diagonals are 13, 17, 21, 25
etc...

(Algorithm)
Other than the first number 1, we always add 4 more numbers for each iteration, where the size matrix increase by 2 each
Also the distance to choose a number from should also increase by 2
'''

numb = 1    #initial sum
nsize = 1    #initial size
summ = 1
finalsize=501   #size 501 has 1001 = 501*2-1 is the length of a row

for nsize in range(1, finalsize):
    for i in range(1, 5):         # add 4 numbers at a time
        numb = numb + nsize*2
        summ = summ +numb
    print "For size", 2*nsize+1, "matrix, the sum is ", summ







