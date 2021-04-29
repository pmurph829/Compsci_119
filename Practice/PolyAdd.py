Frog = [-1,7,0.5,-2,3]
Toad = [5,-3,2.5,2,-3]

def polyNormalize(P):
    Q = [0 for I in range(len(P))]
    for I in range(len(P)):
        Value = P[I]
        if (abs(Value - float(int(Value))) < 1.0E-14): Q[I] = int(Value)# determines if Value is an integer or not                
        else: Q[I] = Value
    while (len(Q)>1) and (Q[-1] == 0): del Q[-1] 
    return Q

def polyAdd(P0, P1, P2 = []): # P0 and P1 are lissts of coefficients
    P = [0 for I in range(max(len(P0),len(P1), len(P2)))]
    for I in range(len(P0)): P[I] = P[I] + P0[I]
    for I in range(len(P1)): P[I] = P[I] + P1[I]
    for I in range(len(P2)): P[I] = P[I] + P2[I]
    return polyNormalize(P)

def polySubtract(P0, P1, P2 = []): # P0 and P1 are lissts of coefficients
    P = [0 for I in range(max(len(P0),len(P1), len(P2)))]
    for I in range(len(P0)): P[I] = P[I] + P0[I] # positive P0 - P1 - P2
    for I in range(len(P1)): P[I] = P[I] - P1[I]
    for I in range(len(P2)): P[I] = P[I] - P2[I]
    return polyNormalize(P)

def polyMultiply(P0,P1):
    P = [0 for I in range(len(P0)+len(P1))]
    for I in range(len(P0)):
        for J in range(len(P1)): #for loop w/in a for loop: goes through all of P1 for each index of P0
            P[I+J] = P[I+J] + P0[I]*P1[J]
    return polyNormalize(P)

def polyDifferentiate(P):
    Q = [0 for I in range(len(P) - 1)]
    for I in range(1, len(P)):
        Q[I-1] = I * P[I]
    return polyNormalize(Q)

def polyStr(P):
    S = ""
    for Exponent in range((len(P)-1),1,-1):
        Coefficient = P[Exponent]
        if Coefficient != 0:
            if Coefficient < 0: S = S + " - "
            else              : S = S + " + "
            if (Exponent == 0) or (abs(Coefficient) != 1):
                S = S + str(abs(Coefficient))
            if (Exponent >= 1):
                S = S + "X"
            if (Exponent < 1): S = S + str(Exponent)
    return S





