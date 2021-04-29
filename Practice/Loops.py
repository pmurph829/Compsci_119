# Do a thing x amount of times
# Counter Loop: Need 3 things:
# 1) define counter to some value
# 2) Test if it has reached a termininating value
# 3) Something that changes counter

# Counter starts at 0, but ends when counter is <= N, so it will actually print N + 1
def Loop(N):
    counter = 0
    while (counter <= N):
        print("hello",counter)
        counter = counter + 1
    return

def Loop1(N):
    counter = 1
    while (counter <= N):
        print("hello",counter)
        counter = counter + 1
    return

def infinite():
    counter = 1
    while counter > 0:
        print("TO INFINITY AND BEYOND! (CTRL C TO STOP)", counter)
        counter = counter + 1
    return

