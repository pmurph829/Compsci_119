# Task = function that asks the user to enter a number that is >= 0, asks again if not positve

def GetPositive ():
    N = float(input("Enter a number greater than or equal to zero --- "))
    while N <= 0:
        N = float(input("Enter a number greater than or equal to zero --- "))
    return N
