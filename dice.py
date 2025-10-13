import random

stop = True
roll = 0

diceRollO = random.randint(1, 9)
diceRollT = random.randint(1, 9)

while stop:
    if diceRollO != diceRollT:
        print("Roll", roll,":", diceRollO,"and",diceRollT)
        diceRollO = random.randint(1, 9)
        diceRollT = random.randint(1, 9)
        roll = roll + 1

    elif diceRollO == diceRollT:
        print("it took",roll,"rolls to get a double")
        stop = False

roll = roll + 1
