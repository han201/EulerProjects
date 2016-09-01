'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

#1. Identify how many days after 12/31/1899 is for each first day of the month between 01/01/1901 and 12/31/2000
#2. if (number of days)%7==0, it is Sunday
#3. Count

sundaySum = 0
firstday = 365+1                         # 01/01/1901, since 1900 has 365 days
lastday = 365*101+1*(100/4)         # 12/31/2000, since there are 100 years plus 25 leap years. 2000 is a exceptional leap year century
monthOfyear = 1
leapyear = 'false'
year = 1901

while (firstday <= lastday):
    if monthOfyear==13:
        monthOfyear=1       # reset for January
        year=year+1         # add one more year
        if year%4==0:                 # Check for a leap year
            leapyear = 'true'
        else:
            leapyear = 'false'

    if firstday%7==0:                    #Check for Sunday
        sundaySum=sundaySum+1
        print "month", monthOfyear, "in year", year, "has Sunday on its first day"
    #print "month", monthOfyear, "in year", year, "has ", firstday%7, " on its first day"
    #move to the next first day
    if monthOfyear ==4 or monthOfyear==6 or monthOfyear==9 or monthOfyear==11:
        firstday = firstday+30
    elif monthOfyear == 2:
        if leapyear=="true":
            firstday = firstday + 29
        else:
            firstday = firstday + 28
    else:
        firstday = firstday + 31
    monthOfyear = monthOfyear+1        #check for next month
    #print "new month is ", monthOfyear, " and new firstday is ", firstday

print "Total number of fist day of a month whose day is Sunday is", sundaySum





