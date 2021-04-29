# TASK 1: build a list called Q containing the square roots of all numbers
# from 0 to 100 by 5s

import math

#Q = []
#Counter = 0
#while Counter < 101:
 #  Q = Q + [X]
  #  Counter = Counter + 5
#print(Q)


#More efficient:
#Q = []
#for Counter in list(range(0,101,5)): Q = Q + [math.sqrt(Counter)]
#print(Q)




# TASK 2: Define a function called GetSqrt that takes one parameter N and returns a
# list of sqrts from 0 to N

def GetSqrt (N):
    Q = []
    for Counter in list(range(N)): Q = Q + [math.sqrt(Counter)]
    return Q
