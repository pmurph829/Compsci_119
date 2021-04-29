# list comprehensions

import math
# L = []
# for I in range(10):
#   L = L + [math.sqrt(I)]

L = [math.sqrt(I) for I in range(10)]
# has same effect as above but accomplished in one line

F(x) = [3*x*x + 2*x - 4 for x in range(11)]

F2(x) = [3*x*x + 2*x - 4 for x in range(100) if x%3 == 0]

# list comprehension is very powerful, can contain 4 lines of code into a
# single line!!

