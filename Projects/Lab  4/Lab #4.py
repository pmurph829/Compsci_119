# Peter Murphy

import random as r

def GetANumber(Message="Enter a number between 0 and 999 --- "):
    Result = -1
    try:
        while Result < 0 or Result > 999: Result = int(input(Message))
    except: Result = GetANumber(Message)
    return Result

def Main():
    HurklePosition = [r.randrange(1000),r.randrange(1000)]
    Tries = 0
    MoreToDo = True
    while Tries < 10 and MoreToDo:
        Guess_X = GetANumber("Enter X from 0 to 999 --- ")
        Guess_Y = GetANumber("Enter Y from 0 to 999 --- ")
        Guess = [Guess_X,Guess_Y]
        if Guess == HurklePosition:
            print("WIN\nLocation: "+str(HurklePosition))
            MoreToDo = False
        else:
            Tries = Tries + 1
            print(str(Tries)+"/10 attempts used")
            if   Guess_X  > HurklePosition[0] and Guess_Y  > HurklePosition[1]: print("Go southwest\n")
            elif Guess_X  < HurklePosition[0] and Guess_Y  > HurklePosition[1]: print("Go southeast\n")
            elif Guess_X  < HurklePosition[0] and Guess_Y  < HurklePosition[1]: print("Go northeast\n")
            elif Guess_X  > HurklePosition[0] and Guess_Y  < HurklePosition[1]: print("Go northwest\n")
            elif Guess_X == HurklePosition[0] and Guess_Y  > HurklePosition[1]: print("Go south\n")
            elif Guess_X == HurklePosition[0] and Guess_Y  < HurklePosition[1]: print("Go north\n")
            elif Guess_X  > HurklePosition[0] and Guess_Y == HurklePosition[1]: print("Go west\n")
            elif Guess_X  < HurklePosition[0] and Guess_Y == HurklePosition[1]: print("Go east\n")
    if MoreToDo: print("Hurkle got away!\nLocation: "+str(HurklePosition))
                                                                                     
    return
