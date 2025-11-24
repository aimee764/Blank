items = [23, 41, 11, 17, 34, 56, 67, 12]#list of items that need to be sorted
n = len(items)-1#n for number of items
print("length of the list:",n)
index = 0
for index in range(0, n):#loops the list
    if (items[index] > items[index + 1]):
        temp = items[index]
        items[index] = items[index + 1]
        items[index + 1] = temp #swaps the smallest number with the biggest until the list is sorted


print(items)
