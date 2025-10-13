def princible():
    prin = int(input("Please enter princible amount: "))
    return(prin)

def rate():
    ret = int(input("Please enter rate: "))
    return(ret)

def time():
    tim = int(input("please enter time in years: "))
    return(tim)

def calculator(pPrin, pRet, pTim):
    interest = (pPrin * pRet * pTim)//100
    print("The interest is", interest)

prin = princible()
ret = rate()
tim = time()
calculator(prin, ret, tim)
