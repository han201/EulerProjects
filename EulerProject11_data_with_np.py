# Challenge problem: 1. I spent a lot of time thinking of algorithm. 2. Still the answer is wrong. 3. The answer matches with my excel calculation

#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?
import numpy as np
#import pandas as pd
fhand =  np.loadtxt('EulerProject11_data.txt')   # Open the data
# inp = fhand.read()                       # read as a string
# inp = ''.join([line.strip() for line in inp])   # removes newline space
# print fhand
# fhand is a 2-dim array with the size len(fhand) by len(fhand[0, :])

maximum = 1                               #maximum number for result
numOfMul = 4

numRows = len(fhand[:, 0])
numCols = len(fhand[0, :])

print "Number of rows = ", numRows, " and number of columns =", numCols

#1. for left and right maximum
for rows in range(0, numRows):
    for i in range(0, numCols-numOfMul+1):
        product = 1
        for j in range(i, i+numOfMul):
            product = product * fhand[rows, j]
        if (maximum < product):
            maximum = product
            print "Max is for left and right: ", fhand[rows, i:i+numOfMul], product

#2. for up and down maximum
for cols in range(0, numCols):
    for i in range(0, numRows-numOfMul+1):
        product = 1
        for j in range(i, i+numOfMul):
            product = product*fhand[j, cols]
        if (maximum < product):
            maximum = product
            print "Max is for up and down: ", fhand[i:i+numOfMul, cols], product

#3. Lower Triangular maximum (including Diagonal)
numDiagonal=numRows   # inlude the diagonal

while (numDiagonal>= numOfMul):
    for i in range(numRows-numDiagonal, numRows - numOfMul + 1):
        product = 1

        for j in range(i, i+numOfMul):
            product = product * fhand[j, j-(numRows-numDiagonal)]
        if (maximum < product):
            maximum = product
            print "Max is for Lower Triangular: ", fhand[j-3, j-(numRows-numDiagonal)-3], fhand[j-2, j-(numRows-numDiagonal)-2], fhand[j-1, j-(numRows-numDiagonal)-1], fhand[j, j-(numRows-numDiagonal)], product
    numDiagonal-=1

#4. Upper Triangular maximum: need to use while
numDiagonal=numCols-1     # exclude diagonal

while (numDiagonal>= numOfMul):
    for i in range(numCols-numDiagonal, numCols - numOfMul + 1):
        product = 1
        for j in range(i, i+numOfMul):
            product = product * fhand[j-(numCols-numDiagonal), j]
        if (maximum < product):
            maximum = product
            print "Max is for Upper Triangular: ", fhand[j-(numCols-numDiagonal)-3, j-3], fhand[j-(numCols-numDiagonal)-2, j-2], fhand[j-(numCols-numDiagonal)-1, j-1], fhand[j-(numCols-numDiagonal), j], product
    numDiagonal-=1

