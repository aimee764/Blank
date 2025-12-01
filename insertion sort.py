import random
y = 10
items = [random.randint(1, 100) for i in range(y)]
length = len(items)#the length of the list
for index in range(1, length):#goes through the entire list 
    current = items[index]#the current number is the second number in the list so it can compare
    index2 = index#index2 so it can be altered and not mess up the loop going through the list
    
    while index2 > 0 and items[index2 - 1] > current:#checks if index2 is bigger than 0 and it's bigger than the second number so they can swap
        items[index2] = items[index2 - 1]#swaps first and second number
        index2 = index2 - 1#

    items[index2] = current#
    print(items)

    
