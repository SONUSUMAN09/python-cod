# if statment
age=input("enter your age")
age=int(age)
if age>=10:
    print("you are above 10")
    print("you can play the game")

# pass statment
x=18
if x>18:
    pass

# else statment
age=input("enter your age")
age=int(age)
if age>=10:
    print("you are above 10")
    print("you can play the game")
else:
    print("sorry you are under 10")
    print("you can not play game")


# lec 42 exercise nasted if else 
# a game input no. then if same thenprint win is less then printtoo less if more then print too big
win_no=25
user_input=input("input any number")
user_input=int(user_input)
if user_input==win_no:
    print("you win")
else:
    if user_input<win_no:
        print("too less")
    else:
            print("too high")



#and or operator
name="abc"
age=11
if name=="abc" and age==11:
    print("T")
else:
    print("F")
# take input and check
name=input("enter your name")
age=input("enter your age")
if name=="sonu" and age=="25":
    print("T")
else:
    print("F")

    # or opeartor me koi bhi ek condition se kam chlega 
name=input("enter your name")
age=input("enter your age")
if name=="sonu" or age=="25":
    print("T")
else:
    print("F")

    # or and operator togather
    name=input("enter your name")
age=input("enter your age")
if age>="25" and name[0]=="A" or name[0]=="a":
    print("T")
else:
    print("F")


    #  if elif else stanment multiple condition show ticket price age 
age=input("enter age")
age=int(age)
if 0<age<=3:
    print("price free")
elif 3<age<=10:
    print("price 10")
elif 10<age<=20:
    print("price 200")
elif 20<age<=60:
    print("price 30")
else:
        print("price 100")


        #  in keyword
name="sonusuman"
if "a" in name:   # name ki jgh direct koi string bhi dal skte he jese "sonusuman"
    print("a is present in name")
else:
    print("not present in name") 




 # check empty or not
name="vgyfy"
if name:  # this is true and run if string is not empty
    print("string is not empty")
else:
        print("string is empty")




# samme last program check empty or not but user input
name=input("enter your name:")
if name:
    print(f"your name is {name} :")
else:
        print("no name enterd")



# while loop print sonu suman 10 times
i=1
while i<=10:
    print("sonu suman")
    i=i+1
i=1
while i<=10:
    print(f"sonu suman {i}")
    i=i+1


# sum of numbers
number=input("input number for sum")
number=int(number)
total=0
i=1
while i<=number:
    total=total+i
    i=i+1  # i+=1
print(total) 





# add all entity 12345=15
number=input(" input a number")
x=len(number)
S=0
i=0
while i<x:
    S=S+int(number[i])
    i=i+1
    print(S)



# input a string then print all latter with their count like s=3 lec 57 some problemin this
name=input("enter name")
temp_var=""
i=0 # 0 to length-1
while i<len(name):
    if name[i] not in temp_var:
        tamp_var=temp_var+name[i]
    print(f"{name[i]} : {name.count(name[i])}")
i=i+1


#loops
# for loop range function
for i in range(10):  # i 0 to 9   #range(1,11)
    print(f"sonu suman : {i}")



#sum of numbers

total=0
for i in range(1,11):
    total=total+i
print(total)


#sum of n numbers
n=int(input("input number for sum"))
total=0
for i in range(1,n+1):  # 1 se 10 tak sum k liye 1 se 11 likhte he 
    total=total+i
    print(total)




# sum of num like 12345==1+2+3+4+5=15
total=0
num=input("enter the number")
for i in range(0,len(num)):
    total=total+num[i]
    print(total)
    




#step argument in range function
for i in range(0,10,1): # last term step btayegi
    print(i)
for p in range(0,10,2): # last term step btayegi
    print(p)    
for q in range(10,1,-1): # last term step btayegi
    print(q)
for r in range(0,10,-1): # last term step btayegi
    print(r)
for s in range(0,-10,2): # last term step btayegi
    print(s)
