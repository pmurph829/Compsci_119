# Peter J. Murphy

import random as r

Rolls   = int(input("Enter number of rolls --- "))
Counts  = [0 for i in range(11)]
Percent = [0 for i in range(11)]
for roll in range(Rolls):
    Dice = r.randint(1,6) + r.randint(1,6)
    Counts[Dice - 2] = Counts[Dice - 2] + 1
    Percent[Dice - 2] = round((Counts[Dice - 2] / Rolls)*100,4)
for value in range (2,13): print("Value = " , str(value) , "Count = " , str(Counts[value - 2]) , " = " , Percent[value - 2] , "%")

