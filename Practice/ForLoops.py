#For loops,
L = [23,67,85,76,89,100]
for i in L:
    print(i)

print("other strategy:")
# same thing, but you know the postion of each item in the list:
for counter in range(len(L)):
    print(counter, L[counter])
