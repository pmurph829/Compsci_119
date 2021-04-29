N = int(input("Enter an integer /n--- "))
while N > 1:
    print(N)
    if N % 2 == 0:
        N = N // 2
        #use // to get an integer as opposed to a float
    else:
        N = (N * 3) + 1
print(N)
