def GetPositive(Message = "Please enter a positive number --- "):
    N = -1
    while N <= 0:
        N = int(input(Message))
        Message = "I said a positive number you idiot try again --- "
    print("Good job")
    return


def PrintGrade(Grade):
    if   Grade >= 90: print("A")
    elif Grade >= 80: print("B")
    elif Grade >= 70: print("C")
    elif Grade >= 60: print("D")
    else:             print("hah dumb")

    return
# can put the action on the same line as the if, elif, or else clause if there is just one action
# helps to line things up
