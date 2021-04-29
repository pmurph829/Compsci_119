import DrBillsInputOutput as b

def Main():
    Filename = b.pickAFolder() + "/MyResults.txt"
    print(Filename)

    MyFile = open(Filename, "w")

    for I in range(20):
        MyFile.write(str(I) + " " + str(math.sqrt(I))+ "\n")

    MyFile.close()
    return
