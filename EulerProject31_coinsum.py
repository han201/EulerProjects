# 1, 2, 5, 10, 20, 50, 100, and 200
# How many combinations possible to have 200?

'''
Let's say there are
a * 200
b * 100
c * 50
d * 20
e * 10
f * 5
g * 2
h * 1

The formula is

200 = a* 200 + b* 100 + c*50 +d * 20+e * 10+ f * 5 + g * 2 + h
'''

def coins(a, b, c, d, e, f, g, h):
    x = a* 200 + b* 100 + c*50 +d * 20+e * 10+ f * 5 + g * 2 + h
    return x


a, b, c, d, e, f, g, h =0, 0, 0, 0, 0, 0, 0, 0
z=coins(a, b, c, d, e, f, g, h)
countCoin=8    # initial count when there is only one kind of a coin, except for the penny
while (b <2):
    while (c <4):
        while (d <10):
            while (e <20):
                while (f <40):
                    while (g <100):
                        while (h < 200):
                            h=h+1
                            z = coins(a, b, c, d, e, f, g, h)
                            if z == 200:
                                countCoin = countCoin+1
                                print "Cofficients:", a, b, c, d, e, f, g, h, "make sure it is 200:", z, "total:", countCoin
                        z, h = 0, 0
                        g=g+1
                    g, h, z = 0, 0, 0
                    f=f+1
                f, g, h, z = 0, 0, 0,0
                e = e+1
            e, f, g, h, z = 0, 0, 0, 0, 0
            d = d+1
        d, e, f, g, h, z = 0, 0, 0, 0, 0, 0
        c = c+1
    c, d, e, f, g, g, z = 0, 0, 0, 0, 0, 0, 0

