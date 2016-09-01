'''
Find nubmer of routs in 20*20 grid.
Mathematically, the anser is 40!/(20!*20!)
I guess 40! is such a big number, so that we need to use some clever way.
Or alternatively, the program probably asks to try out all the possible routes until there is no other ways.
However, I will just use my mathematical formula first
'''

from EulerProject_HanFunctions import factorial

print factorial(40)/(factorial(20)*factorial(20))
