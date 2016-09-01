#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

fhand = open('EulerProject8_data.txt')   # Open the data
inp = fhand.read()                       # read as a string
inp = ''.join([line.strip() for line in inp])   # removes newline space. Googling this line was a challenge

maximum = 1                               #maximum number for result
numOfMul = 13                             #number of numbers that are mulplied
for i in range(0, len(inp)-numOfMul):
    product = 1  # initial value
    for j in range(i, i+numOfMul):
        product = product * int(inp[j])
    if (maximum<product):
        maximum=product
        print inp[i:i+numOfMul], maximum



