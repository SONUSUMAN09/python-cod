# for loop and string   lec68
name="sonu"
for i in range(len(name)):
    print(name[i])


# or we can use 
nam="sonu"
for x in nam:
    print(x)
    


# or directly
for i in "sonu":
    print(i)\

# sum of number like 123=1+2+3=6
number=input("enter the number")
total=0
for i in number:
    total=total+int(i)
print(total)

