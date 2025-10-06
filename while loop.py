answer = True

age = int(input("Enter your age here: "))

while answer:
    if age > 0 and age < 130:
        print("You have entered a correct age")
        answer = False

    else:
        print("Your age is wrong, try again")
        age = int(input("Enter your age here: "))
        

        
