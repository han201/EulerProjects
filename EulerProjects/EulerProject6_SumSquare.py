# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

N = 100   # 100 natural numbers
sumsquare = 0
squaresum = 0
sum = 0
for n in range(1, N+1):
    sumsquare = sumsquare + n**2
    sum=sum+n
    squaresum = sum**2
    diff = squaresum - sumsquare
    print "for n equals ", n, ", sum of the square is ", sumsquare, ", square of sum is ", squaresum, ". Difference is ", diff
