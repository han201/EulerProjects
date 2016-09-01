# read 100 large numbers and calculate the first 10 digits
#fhand = raw_input('Enter the file name: \n')
#subjectlines = 0
try:
    fopen=open('EulerProject13_LargeSum_Data.txt')
    sum=0
    for line in fopen:
        line=int(line.rstrip())
        sum=sum+line
    print sum

except:
    print 'File cannot be opened: ', fopen
    exit()