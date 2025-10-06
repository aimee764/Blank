import random

number = random.randint(1, 20)
print("You have to guess the number from 1-20 (you have 6 guesses)")
answer = int(input("Please enter your guess here: "))

def guessGame(pNum, pAns):
    counter =  0
    while (counter < 6):
        if (pAns < pNum):
            print("Your number is too small")
            counter = counter + 1
            tries = 6 - counter
            print("You have", tries," guesses left")
            pAns = int(input("Please enter your guess here: "))


        elif (pAns > pNum):
            print("Your number is too big")
            counter = counter + 1
            tries = 6 - counter
            print("You have", tries,"guesses left")
            pAns = int(input("Please enter your guess here: "))
        
        else:
            print("well done you got it right")
            tries = 6 - counter
            print("You got it in", tries,"tries!")
            counter = 6

    else:
        print("the number was", pNum)                  
guessGame(number, answer)

