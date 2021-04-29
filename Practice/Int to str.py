# How does str() work?

def IntToStr(N):
    S = ""
    Negative = (N < 0)
    N = abs(N)
    while N > 0:
        Remainder = N % 10
        N = N // 10
        Digit = chr(ord("0") + Remainder)
        S = Digit + S
        # Careful, S + Digit returns reverse order!!
    if S == "": S = "0"
    if Negative: S = "-" + S
    return S
