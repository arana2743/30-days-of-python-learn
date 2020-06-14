from decimal import *

a = Decimal('.10')
b = Decimal('.30')
x = .1 + .1 + .1 - .3
y = a + a + a - b
print('x is {}'.format(x)) # expected answer should be 0
print('y is {}'.format(y)) # now gives us desired answer
