
count = True
def toBinary(pNum):
    strOutput = []
    num = 128
    while (num != 0):
        if pNum % 2 == 1:
            strOutput.insert(0, "1")
            pNum = pNum // 2


        elif pNum % 2  == 0:
            strOutput.insert(0, "0")
            pNum = pNum // 2


        num = num // 2
    binaryString = " ".join(strOutput)
    return(binaryString)
            


    

number = int(input("Enter a number to be converted into binary(1-255): "))
while count:
    if (number > 255) or (number < 1):
        number = int(input("Enter a number between 1-255: "))

    else:
        print("Thanks")
        count = False
print(toBinary(number))


