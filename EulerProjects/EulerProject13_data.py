#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

fhand = open('EulerProject13_data.txt')   # Open the data
#inp = fhand.read()                       # read as a string
# inp = ''.join([line.strip() for line in inp])   # removes newline space
maximum = 1                               #maximum number for result
numOfMul = 4

# for left and right maximum
for line in fhand:
    for i in range(0, len(line)-3*(numOfMul-1)-1, 3):
        product = 1
        for j in range(i, i+3*(numOfMul-1)+1, 3):
            product = product * int(line[j:j+2])
        if (maximum < product):
            maximum = product
            print line[i:i+3*numOfMul], product

