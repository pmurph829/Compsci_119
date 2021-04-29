# Greatest Common Divisor
def GCD (A,B):
    while (B > 0):
        Temp = B
        B = A % B
        A = Temp
    return A

N = int(input('Enter a number\n--- '))
N2 = int(input('Enter a 2nd number to get greatest common divisor\n--- '))
Ans = GCD (N, N2)
print('Greatest common divisor = ' + str(Ans))
