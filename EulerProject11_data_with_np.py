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
maximum = 1
for rows in range(0, numRows):
    for i in range(0, numCols-numOfMul+1):
        product = 1
        for j in range(i, i+numOfMul):
            product = product * fhand[rows, j]
        if (maximum < product):
            maximum = product
            print "Max is for left and right: for row and i ", rows, i, fhand[rows, i:i+numOfMul], product
print "Done with left to right\n"
#2. for up and down maximum
maximum = 1
for cols in range(0, numCols):
    for i in range(0, numRows-numOfMul+1):
        product = 1
        for j in range(i, i+numOfMul):
            product = product*fhand[j, cols]
        if (maximum < product):
            maximum = product
            print "Max is for up and down: for cols and i ", cols, i, fhand[i:i+numOfMul, cols], product
print "Done with up and down\n"
#3. Lower Triangular maximum (including Diagonal)
maximum = 1
numDiagonal=numRows   # inlude the diagonal

while (numDiagonal>= numOfMul):
    for i in range(numRows-numDiagonal, numRows - numOfMul + 1):
        product = 1

        for j in range(i, i+numOfMul):
            product = product * fhand[j, j-(numRows-numDiagonal)]
        if (maximum < product):
            maximum = product
            print "Max is for Lower Tri when numDiagonal & i: ", numDiagonal, i, fhand[j-3, j-(numRows-numDiagonal)-3], fhand[j-2, j-(numRows-numDiagonal)-2], fhand[j-1, j-(numRows-numDiagonal)-1], fhand[j, j-(numRows-numDiagonal)], product
    numDiagonal-=1

print "Done with Left to Right Lower diagonal\n"
#4. Upper Triangular maximum: need to use while
maximum = 1
numDiagonal=numCols-1     # exclude diagonal
while (numDiagonal>= numOfMul):
    for i in range(numCols-numDiagonal, numCols - numOfMul + 1):
        product = 1
        for j in range(i, i+numOfMul):
            product = product * fhand[j-(numCols-numDiagonal), j]
        if (maximum < product):
            maximum = product
            print "Max is for Upper Tri when numDiagonal & i: ", numDiagonal, i, fhand[j-(numCols-numDiagonal)-3, j-3], fhand[j-(numCols-numDiagonal)-2, j-2], fhand[j-(numCols-numDiagonal)-1, j-1], fhand[j-(numCols-numDiagonal), j], product
    numDiagonal-=1
print "Done with Left to Right Upper diagonal\n"


#5. Lower Triangular maximum (including Diagonal) (from Right to Left)
maximum = 1
numDiagonal=numRows   # inlude the diagonal
while (numDiagonal>= numOfMul):
    for i in range(numRows-numDiagonal, numRows - numOfMul + 1):
        product = 1
        for j in range(i, i+numOfMul):
            product = product * fhand[j, (numRows-1)-j+(numRows-numDiagonal)]   # j-(numRows-numDiagonal)
        if (maximum < product):
            maximum = product
            print "Max is for Lower Tri when numDiagonal & i: ", numDiagonal, i, fhand[j-3, (numRows-1)-j+(numRows-numDiagonal)+3], fhand[j-2, (numRows-1)-j+(numRows-numDiagonal)+2], fhand[j-1, (numRows-1)-j+(numRows-numDiagonal)+1], fhand[j, (numRows-1)-j+(numRows-numDiagonal)], product
    numDiagonal-=1

print "Done with Right to Left Lower diagonal\n"


#6. Upper Triangular maximum: need to use while (from Right to Left)
maximum = 1
numDiagonal=numCols-1     # exclude diagonal
while (numDiagonal>= numOfMul):
    for i in range(numCols-numDiagonal, numCols - numOfMul + 1):
        product = 1
        for j in range(i, i+numOfMul):
            product = product * fhand[j-(numCols-numDiagonal), (numCols-1)-j]   # fhand[j-(numCols-numDiagonal), j]
        if (maximum < product):
            maximum = product
            print "Max is for Upper Tri when numDiagonal & i: ", numDiagonal, i, fhand[j-(numCols-numDiagonal)-3, (numCols-1)-j+3] , fhand[j-(numCols-numDiagonal)-2, (numCols-1)-j+2] , fhand[j-(numCols-numDiagonal)-1, (numCols-1)-j+1] , fhand[j-(numCols-numDiagonal), (numCols-1)-j] , product
    numDiagonal-=1
print "Done with Right to Left Upper diagonal\n"
