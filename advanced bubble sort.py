items = [23, 41, 11, 17, 34, 56, 67, 12]
n = len(items)-1
swapped = True
index = 0
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
