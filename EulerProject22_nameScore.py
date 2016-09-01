'''
1. read the data
2. sort by alphabetical order.
3. Convert each name into a score (sum)
4. calculate score*order (order sum)
5. sum total scores
'''

fhand = open('EulerProject22_data.txt')   # Open the data
inp = fhand.read()                       # read as a string
#inp = ''.join([line.strip() for line in inp])   # removes newline space

inp = inp.translate(None, '"')           # removes "
arr = inp.split(",")                     # splits by comma

arr.sort()

ordersum = 0
for i in range(0, len(arr)):
    sum=0
    for letter in arr[i]:
        number = ord(letter)-64        # A is 65 in ASCII
        sum = sum + number
    ordersum=ordersum + sum*(i+1)
print ordersum
