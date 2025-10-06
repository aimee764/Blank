import random 

heads = 0
tails = 0

num = int(input("How many times would you like to flip the coin:"))

for x in range(0, num):

    flip = random.randint(0, 1)
    
    if flip == 1:
        #print("heads")        
        heads = heads + 1
        

    elif flip == 0:
        #print("tails")        
        tails = tails + 1


print("There are", tails,"tails and", heads,"heads")
          
