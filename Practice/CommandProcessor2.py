# Write a program with a command processor where the commands allow us to
# clear or add to a list, then perform any of the following operations on
# all elements of the list

import math as m

def Process(L,Function):
    for I in range(len(L)):
        try: L[I] = Function(L[I])
        except: L[I] = "ERROR"
    return

Info = {"QUIT"  :"Closes Program",
        "CLEAR" :"Clears list",
        "ADD"   :"Adds specified item to list",
        "ABS"   :"Takes absolute value of each item in list",
        "SQRT"  :"Takes square root of each item in list",
        "LOG"   :"Takes log of each item in list",
        "INT"   :"Converts each item in the list to an integer",
        "FLOAT" :"Converts each item in the list to a float",
        "SQUARE":"Squares each item in the list",
        "CUBE"  :"Cubes each item in the list",
        "NEGATE":"Returns the negative of each item in list",
        "INFO"  :"Gives information about each command"}
def Main():
    L = []
    MoreToDo = True
    Message = """Commands:
QUIT CLEAR ADD ABS SQRT LOG
INT FLOAT SQUARE CUBE NEGATE
INFO
---------------
Enter a command --- """
    while MoreToDo:
        print("\n")
        print(L)
        Command = input(Message)
        Command = Command.upper()
        if   Command == "QUIT"    : MoreToDo = False
        elif Command == "CLEAR"   : L = []
        elif Command == "ADD"     : L = L + [float(input("Enter a value to add --- "))]
        elif Command == "SQRT"    : Process(L,m.sqrt)
        elif Command == "LOG"     : Process(L,m.log)
        elif Command == "ABS"     : Process(L,abs)
        elif Command == "INT"     : Process(L,int)
        elif Command == "FLOAT"   : Process(L,float)
        elif Command == "SQUARE"  : Process(L,lambda a : a*a)
        elif Command == "CUBE"    : Process(L,lambda a : a*a*a)
        elif Command == "NEGATE"  : Process(L,lambda a : -a)
        elif Command == "INFO"    :
            Lookup = input("Enter a commnad for more information --- ")
            print("\n"+Lookup.upper()+": "+Info[Lookup.upper()])
        else: print("Illegal Command")
        print("Result:\n",L)
    return
