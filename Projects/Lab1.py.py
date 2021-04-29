# Peter J. Murphy (29986613) - Assignment #1

def PadRight(S,N):
    pad = N - len(S)
    while pad > 0:
        S = S + " "
        pad = N - len(S)
    return S

def PadLeft(S,N):
    pad = N - len(S)
    while pad > 0:
        S = " " + S
        pad = N - len(S)
    return S

def GetGrade (Score):
    if Score >= 90:   Result = "A"
    elif Score >= 80: Result = "B"
    elif Score >= 70: Result = "C"
    elif Score >= 60: Result = "D"
    elif Score < 0:   Result = " Hopefully an error!"
    else:             Result = "F"
    return Result

def Process(Name, Score):
    S = ""
    S = S + PadRight(Name,10)
    S = S + PadLeft(str(Score),3)
    S = S + PadLeft(str(GetGrade(Score)),2)
    S = S + " "
    Counter = 1
    while Counter <= Score:
        S = S + "|"
        Counter = Counter + 1
    return S

def Main():
    print (Process ("Fred", 78))
    print (Process ("Sam", 23))
    print (Process ("Mary", 100))
    print (Process ("Bob", 72))
    print (Process ("Carol", 62))
    print (Process ("Sue", 85))
    print (Process ("Mortimer", 5))
    return
