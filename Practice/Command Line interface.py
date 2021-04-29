# Command Line Interface

# Commands:
# QUIT
# OPEN
# SAVE
# PRINT
# NEW

def Command_Open()
    return

def Command_Save()
    return

def Command_Print()
    return

def Command_New()
    return

def Main()
    MoreToDo = True
    while MoreToDo:
        Command = input("Enter a command --- ")
        Command = Command.upper()
        if   Command == "QUIT"  : MoreToDo = False
        elif Command == "OPEN"  : Command_Open()
        elif Command == "SAVE"  : Command_Save()
        elif Command == "PRINT" : Command_Print()
        elif Command == "NEW"   : Command_New()
        else: print("Illegal Command")
    

    return


# use pass after a colon to not do anything, used as a temp placeholder
