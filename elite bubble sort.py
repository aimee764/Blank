import random
y = 100
items = [random.randint(0,10000) for x in range(y)]
swapped = True
index = 0
print(items)
while(swapped and n > 0):
    swapped = False
    for index in range(0, n):
        if(items[index] > items[index + 1]):
           temp = items[index]
           items[index] = items[index + 1]
           items[index + 1] = temp
           swapped = True

    n = n - 1
print(items)
