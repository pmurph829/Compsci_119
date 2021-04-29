#tracing functions manually. Look at notes for explanation
def F2(z,y,x = 3):
    # x = 3 means if no value is given for x, assume it is 3. Must be the last one specified
    v = z + y
    return v * x

def F1(x,y,z):
    w = x + y * z
    v = F2(z,w,x)
    return v

print(F2(2,4,3))

print(F1(3,5,2))

print(F2(7,4))
