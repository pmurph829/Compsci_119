# square root
def SquareRoot (N):
    Guess = N / 2
    Quotient = N / Guess
    NewGuess = (Guess + Quotient) / 2.0

    while (abs(Guess - NewGuess) > 1.0E-15):
        Guess = NewGuess
        Quotient = N / Guess
        NewGuess = (Guess + Quotient) / 2

    return NewGuess
import math

# Find the distacne between two points
# To run, type "Distance(" into the interactive area after >>>, then input values for X1,Y1,X2,Y2
def Distance(X1,Y1,X2 = 0,Y2 = 0):
    # second point has defalut value (0,0), so if second point is not specified, it will return distance from the origin
    A = X2 - X1
    B = Y2 - Y1
    return SquareRoot(A*A + B*B)
    
def Taxes(Gross,Children = 0, Taxrate = 0.05):
    return Gross * Taxrate / (Children + 1)


def Distance2 (P1,P2):    #P1 and P2 are both [X,Y] lists indicating points
    DeltaX = P2[0] - P1[0]
    DeltaY = P2[1] - P1[1]
    return math.sqrt(DeltaX*DeltaX + DeltaY*DeltaY)
