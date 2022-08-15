# variable
#x=2
#print(x)
#x="sonu"  # ek variable me do chije dal skte he 
#print(x) # variable can be nom,_nom,a%bc,a12bc but cant be %nom,1nom



# add of variable
#a="sonu"
#x=2
#y="suman"
#z=3
#b=x+z
#print(b)
#print(a+ y) # nya variable bhi le skte he or direct add bhi kr skte he 
#print(a*x) # sonu do bar aayega 
#print(a+x)# wrong string + integer
#print(a+str(x)) # convert x from integer to string
#print(a+"x") # print sonux q ki x char he mtlb x=2 nhi only x

# user input
#name =input("enter your name")
#age=input("enter your age")
#print( "hello " + name + " your age is " + age)
#print( "hello" + name + "your age is" + age)

# addition of numbers
#n1=input("first no is ")
#n2=input("second no is ")
#n3=input("third no is ")
#total=n1+n2+n3
#print("total="+total) # 28 to 33 wrong q ki sbhi no. string he inko integer mne convert krege ese


#n1=int(input("first no is "))
#n2=int(input("second no is "))
#n3=int(input("third no is "))
#total=n1+n2+n3
#print("total="+str(total)) #finaly ye string hona chahiye but hmne change kr diya tha so last  me waps change kr rhe he 

# str int float
#a1=str(2)
#a2=int(2)
#a3=float(2)
#print(a1+a2+a3)# error str + int 
#print(a2+a3)# give 4.0 float


 # two variable at one time
name,age="  sonu","25"
print("hello"+name+" your age is "+age)



 # two variable at one time
name,age=input("enter your name and age").split()
print("hello"+name+" your age is "+age)



 # string formation py2
name="sonu"
age=25
print("hello"+name+"your age"+str(age))
# py3
print("hello {} your age is {} ".format(name,age))
#py3.6
print(f"hello {name} ypur age is {age}")  # age+2 or any thing can be done




 #string indexing
name=("abcdefgh")
print(name[0])
print(name[1])
print(name[4])
print(name[0:4])# only 0 to 3 print hoge 
print(name[-1])
print(name[-2])
print(name[-4])

# revers of name
name=input("enter your name")
print(f"revers nameis{name[-1::-1]}")

# string mathods party one
name="abcdefabcd efabcdea"
length=len(name) # 
print(length) # lenght include space
print(name.lower()) # all latter lower case
print(name.upper()) # all leteruppercase
print(name.title()) # first latter capital
print(name.count("a")) # count the latter in bracket



# take name then give lenght then give count of any latter
name,char=input("enter comma seprated name and character: ").split(",")
print(f"length of the name is{len(name)}")
print(f"char count: {name.count(char)}") # case senstive
print(f"char count: {name.lower().count(char.lower())}") # case senstive space dene nhi dene se problem aati he isko htane k liye next
print(f"char count: {name.strip().lower().count(char.strip().lower())}") 




# string space
name="     so  nu     "
dots=".............."
print(name + dots)
print(name.lstrip() + dots) # left space khtm
print(name.rstrip() + dots) # right space khtm
print(name.strip() + dots) # sbhi space htana
print(name.replace(" ",""))  # space khtm krna 
print(name.replace(" ","")+ dots)



# find and replace
name="is my name is is your name is is "
print(name.replace(" ","_"))
print(name.replace("s","_")) # word or latter can b replace
print(name.replace("s","_", 1)) # only first wala replace
print(name.find("is"))
print(name.find("is",3)) # start search from 3rd position
is_pos1=name.find("is") # it is number
is_pos2=name.find("is",is_pos1+1)
print(is_pos2)



# center mathod "sonu" to "**sonu**"
name="sonu"
print(name.center(6,"*"))
print(name.center(8,"*"))

# 4 star before and after any name
name=input("enter your name")
print(name.center(len(name)+8,"*"))



#string are immutable 
#string="abcdef"
#string.replace("a","A")
#print(string) # ek  bar jo string first me bn gyi cgange nhi hoti 


string="abcdef"
new_string=string.replace("a","A")
print(new_string)  # kuch bhi change krne k liye nyi string bnani pdegi




 # more operators
name="sonu"
name=name+"suman"
print(name) 

age=25
age=age+2  #we can use [age += 2] also any operator we can use
age += 1
age -+3
age *= 3

print(age)




