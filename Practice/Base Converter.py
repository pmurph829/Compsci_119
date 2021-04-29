# Base Converter -  Enter a number and a base to convert it to

def BaseConverter (N, Base = 10):
    S = ""
    Negative = (N < 0)
    N = abs(N)
    while N > 0:
        Remainder = N % Base
        print(Remainder)
        N = N // Base
        if Remainder > 9: Digit = chr(ord("0") + Remainder - 10)
        else:             Digit = chr(ord("0") + Remainder)
        # need to subtract 10 from remainder if greater than 10 to get the correct offset
        S = Digit + S
    if S == "": S = "0"
    if Negative: S = "-" + S
    return S
