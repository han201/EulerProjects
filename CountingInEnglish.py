from EulerProject_HanFunctions import digits

# convert the English into numbers
def countingNumbers(N):
    return len(countingGeneral(N))

# combine special cases and rule-based cases
def countingGeneral(N):
    if (N <16 or N==18 or (N%10 == 0 and N <=100) or N==1000):  #special cases
        return countingSpecial(N)
    elif N<100:
        return countingRule2(N)
    elif N<1000:
        return countingRule3(N)
    else:
        return "Rule Error"


#counting special case In English
def countingSpecial(N):
    if N==0:
        return ''
    elif N==1:
        return 'one'
    elif N==2:
        return 'two'
    elif N==3:
        return 'three'
    elif N==4:
        return 'four'
    elif N==5:
        return 'five'
    elif N==6:
        return 'six'
    elif N==7:
        return 'seven'
    elif N==8:
        return 'eight'
    elif N==9:
        return 'nine'
    elif N==10:
        return 'ten'
    elif N == 11:
        return 'eleven'
    elif N == 12:
        return 'twelve'
    elif N == 13:
        return 'thirteen'
    elif N == 14:
        return 'fourteen'
    elif N == 15:
        return 'fifteen'
    elif N == 18:
        return 'eighteen'
    elif N == 20:
        return 'twenty'
    elif N == 30:
        return 'thirty'
    elif N == 40:
        return 'forty'
    elif N == 50:
        return 'fifty'
    elif N == 60:
        return 'sixty'
    elif N == 70:
        return 'seventy'
    elif N == 80:
        return 'eighty'
    elif N == 90:
        return 'ninety'
    elif N == 100:
        return 'onehundred'
    elif N == 1000:
        return 'onethousand'
    else:
        return "Special Error"

# for numbers that meet the general counting rule
def countingRule2(N):         # For two digit numbers with regular rule
    X=digits(N, 10)
    if X[1] == 1:
        return countingSpecial(X[0])+'teen'
    else:          # Special two digits
        return countingSpecial(X[1]*10)+countingSpecial(X[0])

def countingRule3(N):  # For two digit numbers with regular rule
    Y=N/100
    Z=N%100
    if (N%100==0):
        return countingSpecial(Y) + "hundred"
    else:
        return countingSpecial(Y)+"hundredand"+countingGeneral(Z)






