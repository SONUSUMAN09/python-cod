#function intro lec 70
def add(n1,n2):
    return n1+n2

a=int(input("input first number:"))
b=int(input("input secong number :"))
total=add(a,b)
print(total)  # iski jgh direct total(add(a,b)) use kr skte he 

# dusra he string ko jodne k liye 
def add(n1,n2):
    return n1+n2

a=input("input first name:")
b=input("input secong name :")
total=add(a,b)
print(total)      #mtlb def use for define a function  or function me jo n1 n2 dala wo string or integer k liye use kr skte he 
# ise dinamic programinfg khte he integer or string ye khud dekh leta he 

# return and print in function lec 71
def add(n1,n2):
    print(n1+n2)
add(5,4)            # return ki jgh direct print bhi use kr skte he but jyada shi return hota he 



#  function prectice lec 72
#print last char of name
def lastchar(name):
    return name[-1]
name1=input("enter your name : ")
print(lastchar(name1))      #agr print(lastchar(9)) kre to error aayegi isliye jis chij k liye function define kiya he use hi run kre


 # odd even normal 
def oe(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
n1=int(input("enter any number to check odd even"))
print(oe(n1))


# odd even short
def oe(n):
    if n%2==0:
        return "even"
    return "odd"      # else ko hta k return ko if loop se bahr nikal diya 
n1=int(input("enter any number to check odd even"))
print(oe(n1))

#more shortb python coding self btayega ki true he ya nhi 
 # odd even normal 
def oe(n):
     return n%2==0
n1=int(input("enter any number to check odd even"))
print(oe(n1))


# big or small number  lec 74
def big(n1,n2):
    if n1>n2:
        return n1
    return n2     # else ko hta k return ko if loop se bahr nikal diya 
a=int(input("enter first number to check big or small"))
b=int(input("enter second number to check big or small"))
print(big(a,b))



# big amsll number in three  numbers
def big(n1,n2,n3):
    if n1>n2 and n1>n2:
        return n1
    else:
            if n2>n3:
                return n2
    return n3    # else ko hta k return ko if loop se bahr nikal diya 
a=int(input("enter first number to check big or small"))
b=int(input("enter second number to check big or small"))
c=int(input("enter third number to check big or small"))
print(big(a,b,c))




# same last function with function in function lec 76
def big(n1,n2):
    if n1>n2:
        return n1
    return n2      
def bigest(a,b,c):
    bigest=big(a,b)
    return big(bigest,c)
a=int(input("enter first number to check big or small"))
b=int(input("enter second number to check big or small"))
c=int(input("enter third number to check big or small"))
print(bigest(a,b,c))



 # pelindron lec 77
def pelindrom(word):
     reversed_word=word[::-1]
     if word==reversed_word:
      return "T"
     else:
        print("F")
string=input("enter string")
print(pelindrom(string))





# lec 77 video
def is_palindrom(word):
    reversed_word=word[::-1]
    if word==reversed_word:
        return True
    else:
        return False 
print(is_palindrom("name"))
print(is_palindrom("asasasa"))
print(is_palindrom("sosos"))


# short palindrom
def is_palindrom(word):    
    if word==word[::-1]
        return True
    return False 
print(is_palindrom("name"))
print(is_palindrom("asasasa"))
print(is_palindrom("sosos"))


# short palindrom
def is_palindrom(word):    
      return word==word[::-1]
print(is_palindrom("name"))
print(is_palindrom("asasasa"))
print(is_palindrom("sosos"))


# for printing numbers in a line 
for i in range (1,11):
    print(i,end=",")    # coma ki jgh space or kuch bhi lga skte he yha " " mtlb \n apne aap python me aata he 

# fibonacci series  0 1 1 2 3 5 8   # lec 79
def fibonaci(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a, b, end=" ")  # 0 ko first me lane k liye 
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b , end=" ")

fibonaci(10)




 # default parameters  lec 80

def user(name, surname, age):       # normal 
    print(f"name is {name}")
    print(f"surname is {surname}")
    print(f"age is {age}")
user("sonu","suman",26)


def user(name, surname, age=20):       # age ko default kr diya 
    print(f"name is {name}")
    print(f"surname is {surname}")
    print(f"age is {age}")
user("sonu","suman")          # age nhi dege to bhi default age aayegi 



def user(name, surname, age=20):       # age ko default kr diya 
    print(f"name is {name}")
    print(f"surname is {surname}")
    print(f"age is {age}")
user("sonu","suman")          # age  lekin agr age di to default ki jgh jo age di he wo print hogi


def user(name, surname, age=None):       # age ko default kr diya none jo special value he mtlb kuch nhi 
    print(f"name is {name}")
    print(f"surname is {surname}")
    print(f"age is {age}")
user("sonu","suman")          # age nhi dege to bhi default age aayeg


def user(name, surname="unknown", age=None):       # age ko default kr diya none jo special value he mtlb kuch nhi 
    print(f"name is {name}")                       # kisi ko bhi default kr skte he yha surname kiya
    print(f"surname is {surname}")
    print(f"age is {age}")
user("sonu","suman")          # age nhi dege to bhi default age aayeg


def user(name, surname="unknown", age):       # age  yha error aayegi q ki non default(age) aarha he default(surname) k bard
    print(f"name is {name}")
    print(f"surname is {surname}")
    print(f"age is {age}")
user("sonu","suman")          # age nhi dege to bhi default age aayeg




# variable scope lec 81


def func():             # error aayegi
    x=7   # local veriable
    return X
def func2():
    print(x)         # x define only in func jo func2 me use nhin ho skta
func2()       # local variable jo kisi ek function ka ho use dusre me nhinuse kr skte 




def func():             # error aayegi
    x=7   # local veriable
    return X
print(x)          # print function k bahr he 




def func():              
    x = 7   # local veriable
    return x
print(func())    #   no error yha phle 7 print hoga q ki yha is kine me func call ho rh he to scope me aagye 
print(x)          #  error  print function k bahr he 



x=5      # global bariable 
def func():              
    x = 7   # local veriable
    return x
print(func())    #   no error yha phle 7 print hoga q ki yha is kine me func call ho rh he to scope me aagye 
print(x)          #  no error  print function k bahr he but ab global variable aagya jo sbke liye he 
# jha func call kiya wha function k andr ka variable aayega or jha nhi kiya wha global variable ayega 




x=5      # global bariable 
def func(): 
    global x             # ab x global ho gya function  k bahr bhi use kr skte he  
    x = 7   # local veriable
    return x
print(x)         # 5  q ki ab x global he but abhi tk func call nhi hua to ye strting wala globle variable use krega 
print(func())    # 7  q ki ab x global he   
print(x)         # 7  q ki ab x global he     or function call hone k bad use krna he to 7  
 


 