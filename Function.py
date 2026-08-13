#built-in or pre defind function
a =[1,2,3,4,5,6,7,8]
print(a)
len(a)
max(a)
min(a)
type(a)
sum(a)
#user - defined function
def add(x,y):
    x+=y
    print(x)
add(23,43)
add(45,89)
def check_number(num):
    if num%2==0:
        print("even number")
    else:
        print("odd number")
check_number(56)
def login(username,password):
    if username=="admin" and password=="1234":
        print("login success")
    else:
        print("login failed")
login("tharani","1234")
login("admin","1234")
def prime_number(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print("prime number")
    else:
        print("not prime number")
prime_number(7)
def vovals(string):
    count = 0
    for ch in string.lower():
        if ch in "aeiou":
            count+=1
    return count
print(vovals("tharani"))