# square root
def SquareRoot (N):
    Guess = N / 2
    Quotient = N / Guess
    NewGuess = (Guess + Quotient) / 2.0

    while (abs(Guess - NewGuess) > 1.0E-15):
        #DONT COMPARE FLOATS FOR EQUALITY!!! Use difference < 1.0E-15 to be the same as equal for floats
        print("Guess = " + str(Guess) + ", New Guess = " + str(NewGuess))
        Guess = NewGuess
        Quotient = N / Guess
        NewGuess = (Guess + Quotient) / 2

    return NewGuess

N = float(input("Enter a number to get square root:\n--- "))
Answer = SquareRoot(N)
print(Answer)
