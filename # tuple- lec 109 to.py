# tuple- data structure,store any data type, immutable,can't change or update  lec 109
# no append no ,insert no, no pop , no remove
# day('sun','mon','tue')    - jb data fix ho to list ki jgh tuple use krne se speed achchi hogi 
# tuple is fast then list
# methods in tuple count,index,len,slicing
# slicing me bs kuch eement print kraata he kisi ko update nhiu krta 
# day[1]=7 error dega qki change nhi kr skta 
# lekin print(day[:2])  start ki do element dega q ki change nhi kr rha 



# some more tupple             lec 110
# looping in tuple
# tuple with one element 
#tuple without()
# tuple unpacking 
# LIST INside tuple
# some function that can be use in tuple 
mixed=(1,2,3,4.0)

# for loop
for i in mixed:    # for ki jgh while loop bhi use kr skte he 
    print(i)

# tuple with one element
a=(1)
b=('word1')
c=(1,)
d=('word1',)
print(type(mixed))   # tuple
print(type(a))        # not a tuple q ki koma nhi he 
print(type(b))           # ek element ko tuple bnane k liye , use krna pdta he 
print(type(c))
print(type(d))



# tuple without()
name='sonu','suman','kota'    # by defaule this is tuple 


# tuple unpacking
name=('sonu','suman','kota')
nam,surname,city=(name)     # teno chije variable me save ho jayegi number same hone chahiye like 3 age variable km huye to error


# list inside tuple 
name=('sonu',['suman','kota'])
#list me append pop remove insert remove sbhi kr skte he chahe wo tuple me ho 
name[1].pop()
name[1].append('raj')
print(name)

# functions min max sum
mixed=(1,2,3,4.0)
print(min(mixed))
print(max(mixed))
print(sum(mixed))

 # function returning two values   lec 101
def func(int1,int2):
    add=int1+int2
    multiplay=int1*int2
    return add,multiplay
print(func(2,3))  # it will give one tuple do alg alg variable nhi dega 

#alg alg store krne k liye 

 # function returning two values
def func(int1,int2):
    add=int1+int2
    multiplay=int1*int2
    return add,multiplay
add,multiplay=func(2,3)
print(add)
print(multiplay)   


#tuple string list           
num=tuple(range(1,11))
print(num)
#number=(1,2,3,4,5)   # ye tuple he list me change krne k liye 
number=list((1,2,3,4,5))  # ab tuple list me bdl gya 
print(number)


numbers=str((1,2,3,4,4,5))  # yha string me ho gya lekin dikega tuple jesa hi 
print(numbers)
print(type(numbers))

no=str([1,2,3])
print(no)
print(type(no))

# dictionaries          lec 114