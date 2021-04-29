import math
import DrBillsInputOutput as b

def Main():
    Filename = b.pickAFolder() + "/MyResults.txt"
    print(Filename)

    MyFile = open(Filename, "w")

    for I in range(20):
        MyFile.write(str(I) + " " + str(math.sqrt(I)) + "\n")

    MyFile.close()
    return

def ReadAsString(Filename):
    Infile = open(Filename, "r")
    X = Infile.read()
    Infile.close
    return X

def ReadAsList(Filename):
    Infile = open(Filename, "r")
    X = Infile.readlines()
    Infile.close
    return X
