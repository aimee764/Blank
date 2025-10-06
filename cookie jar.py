cookieJar = 10
print("There are", cookieJar,"in the cookie jar")

def minCookie(pMin):
    global cookieJar
    cookieJar = cookieJar - pMin
    print("You ate", pMin,"cookies")
    print("There are", cookieJar,"left")

def addCookie(pAdd):
    global cookieJar
    cookieJar = cookieJar + pAdd
    print("You baked", pAdd,"Cookies")
    print("There are", cookieJar,"left")

def cookieThief():
    global cookieJar
    cookieJar = 10
    cookieJar = cookieJar - 1
    print("The cookie thief robbed a cookie there are", cookieJar,"left in the cookie jar")
    
    print("But you still have", cookieJar,"left")

minus = int(input("how many cookies do you want to eat?: "))
minCookie(minus)
add = int(input("how many cookies would you like to bake?: "))
addCookie(add)
    
