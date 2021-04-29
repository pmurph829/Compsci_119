# factorials
def Factorial1(n):
    F = 1
    Count = 1
    while Count <= n:
        F = F*Count
        Count = Count + 1
    return F

def Factorial2(n):
    F = 1
    for Count in range(1,n+1): F = F*Count
    return F

def Factorial3(n):
    if n <= 1 : return 1
    else      : return n * Factorial3(n-1)

#def Doubler(N):
#    Result = 2 * N
#    return Result


#def Tripler(N):
#    Result = 3 * N
#    return Result

def MyFunction(N): # can be used to create a new function
    return lambda a : a * N # a is the parameter that is passed to the created funciton
# use MyFuncion(2) to create a doubling funcion. Assign it to a variable to use.
# Ex: Tripler = MyFunction(3)
