# Homework 5
def Function1 (W, X=5):
    return W+X
    
def Function2 (Z, W, Y=4):
    return Function1(Z, W+Y)
    
def Function3 (X, Y=2, Z=3):
    return Function2(Y, Z, X)
    
def Main():
    print (Function1(10, 2))              # 1
    print (Function1(6))                  # 2
    print (Function2(4, 3, 1))            # 3
    print (Function2(7, 3))               # 4
    print (Function2(-4, 5))              # 5
    print (Function3(8))                  # 6
    print (Function3(4, 7))               # 7
    print (Function3(1, 3, 5))            # 8
    print (Function2(2, Function1(6)))    # 9
    print (Function3(Function1(9)))       # 10
    return
