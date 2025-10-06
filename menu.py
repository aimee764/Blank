import random

flip = random.randint(0, 1)
num = int(input("How many times do you want to flip the coin: "))

heads = 0
tails = 0

for x in range(1, num):

    flip = random.randint(0, 1)
    
    if flip == 0:
        print("Heads")
        heads = heads + 1
        

    elif flip == 1:
        print("Tails")
        tails = tails + 1
        
        

print("There was", heads,"heads and", tails,"tails")


