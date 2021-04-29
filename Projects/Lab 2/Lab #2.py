# Peter J. Murphy

from DrBillsInputOutput import *

def ReadFileAsOneString (Filename):
    Infile = open(Filename,"r")
    X = Infile.read()
    Infile.close()
    return X

def Main():
# Step 1:
    Filename = pickAFile("Enter a file name here")

# Step 2: 
    OneString = ReadFileAsOneString(Filename)

# Step 3:
    Counts = [0 for characters in range(256)]

# Step 4: 
    Code = [ord(Character)for Character in OneString]
    for item in Code: Counts[item] = Counts[item] + 1

# Step 5:
    Folder = pickAFolder()

# Step 6:
    NewFilename = Folder + "/Counts.txt"
    NewFile = open(NewFilename, "w")

# Step 7:
    NewFile.write("Peter J. Murphy\n" + NewFilename)

# Step 8:
    Total = 0
    Index = 0
    for Count in Counts:
        Total = Total + Count
        if Counts[Index] == 0 : pass
        elif 0 <= Index <= 32 : NewFile.write("\n#" + str(Index) + " = " + str(Counts[Index]))
        elif       Index > 32 : NewFile.write("\n" + chr(Index) + " = " + str(Counts[Index]))
        else                  : NewFile.write("\nERROR") 
        Index = Index + 1
        

# Step 9:
    NewFile.write("\nTotal number of characters analyzed: " + str(Total))

# Step 10:
    NewFile.close()
    return
