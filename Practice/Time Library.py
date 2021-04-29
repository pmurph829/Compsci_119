# Time Library
# must import the library in order for it to work
# time() = gives the number of seconds that have passed since the dawn of time (jan 1, 1970)
# perf_counter() is used to give a difference in time since doing a task

import time as t

def Task1():
    for I in range(10000000): pass

    return

def Task2():
    t.sleep(5.5)
#does nothing for 5.5 seconds
    return

def Main():
    Before = t.time()
#    Task1()
    Task2()
    After  = t.time()
    Elapsed = After - Before
    print("Elapsed time = ", Elapsed)
    return

print(list(t.localtime())
# vs
print(t.asctime(t.localtime()))
