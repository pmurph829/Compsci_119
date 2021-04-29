# Task: write a function that takes in one parameter (N, int)
# Returns a string containing that many exclamation points

def Bang (N):
    S = ""
    while len(S) < N: S = S + "!"
    return S

def Bang2 (N):
    S = ""
    Counter = 1
    while Counter <= N:
        S = S + "!"
        Counter = Counter + 1
    return S
