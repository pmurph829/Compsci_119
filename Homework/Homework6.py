def Glop (P):
    global X
    P = P + 1
    X = P
    return X

def Blort (Q):
    global X
    Glop (X+Q)
    return X

def Snort (R):
    global X
    Blort (X-R)
    return X
