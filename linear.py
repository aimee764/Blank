numList = [1, 55, 79, 243, 7, 78, 5, 33, 55, 89, 67, 21]
value = int(input("Enter number here: "))
end = False
for x in numList:
    while(end == False):
        if value == numList[x]:
            print("Value found")
            end = True
            
        else:
            print("Value not found")
            end = True

            
            


        


