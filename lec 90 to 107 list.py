# list v\s array  lec 90 ch-5
# c++ c jawa me array ek hi typr k data type store krta he
# 
# python me kist hota he jo kuch bhi store kr skta he
# python me array module hota he jo bhi ek hi type ka data type store krta he 
# python array ki performance achhoi he fir bhi use nhi krte
# numpy array for calculations that bind with c 
# list flexible 
# 
#python data science use krne pr complexity and c ki speed milti he dono ko bind krte he 
#
#  javascript array==python list  both flexible

# lec 91 list and string 
# list are immutable   can't change 
# string me koi chij add nhi hoti list me hoti he 
s="string"
st=s.title()    # only first latter ko bda krta he kuch change nhi krta he 
print(st)        # nyi string bna skte he st change krke but original string change nhi hogi
print(s)



# list are mutable
l=['a','bv','abc']
l.pop()    # original list l ko change kr diya 
print(l)



# looping in list   lec 92
# for loop
name=['sonu','suman','kota','raj']
for nam in name:            # ek ek krke sare iteam name se nam me print hoge phle sonu fir suman .........
    print(nam)


# while loop
name=['sonu','suman','kota','raj']
i=0
while i<len(name):
    print(name[i])
    i=i+1




# list inside list   lec 93 
matrix=[[1,2,3],[4,5,6],[7,8,9]]    # it has 3 iteam or list
print(matrix[1])            # give the submatrix 1


# teno sub matrix print hoge
matrix=[[1,2,3],[4,5,6],[7,8,9]]           # ise 2 d list khte he 
for i in matrix:
    print(i)          # teno sub matrix print hoge 


# sbhi numbers ko print krane k liye 
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for submatrix in matrix:     # submatrix ek bar chlega fir i wala 3 bar ese teen bar repete hoga to answer aayega 
 for i in submatrix:
    print(i)


# list inside list ka iteam 
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][1])      # 1st list ka 1st element =5



# type function 
s="string"
print(type(s))    # data type btata he object ka 
print(type(matrix))



# generate list with range function    lec 94
num=list(range(1,11))
print(num)


# pop method
num=list(range(1,11))
print(num.pop())     # jo value pop hui he usko dekhne k liye 
print(num)


# index method 
num=list(range(1,11))
print(num.index(1))    #   show the index number of enterd number yha 1 ki position 0 btayega 


# agr ek hi number 2 bar ho 
number=[1,2,3,4,5,6,7,1,2,3]
print(number.index(1))          # abhi 0 hi dega mtlb firse 1 jha aaya


# agr ek hi number 2 bar ho 
number=[1,2,3,4,5,6,7,1,2,3]
print(number.index(1,3))          #  dusra 1 ki position k liye (1,3) mtlb 3rd position se search krega 0,1,2 ko chor dega 


# agr ek hi number 2 bar ho 
number=[1,2,3,4,5,6,7,1,2,3,1,2,3]      # yha 5 pr ruk jayega seacrh krna 
print(number.index(1,3,5))          #  dusra 1 ki position k liye (1,3) mtlb 3rd position se search krega 0,1,2 ko chor dega 





 

# pass list to a function 
number=[1,2,3,4,5,6,7,8,9,10]
def negative(l):
    numnag=[]
    for i in l:
        numnag.append(-i)
    return numnag
print(negative(number))




# exercise lec 95
# lec 96 print square of list
def square_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
number=list(range(1,11))
print(square_list(number))




 # lec 98   a function which give revers of list
 

# revers method se 
def revers_list(l):
    l.reverse()         # return l.reverse()   me error aayegi q ki ye change kr rha he 
    return l
number=list(range(1,11))
print(revers_list(number))

 # string slicing se
def revers_list(l):
    return l[::-1]
number=list(range(1,11))
print(revers_list(number))    



# append and pop method se
def revers_list(l):
    r_list=[]
    for i in range(1,len(l)+1):
        poped_iteam=l.pop()
        r_list.append(poped_iteam)
    return r_list
number=[1,2,3,4]
print(revers_list(number))



 # ["abc","tuv","xyz"]=["cba","vut","zyx"]   lec 100
def reverse_element(l):
    element=[]
    for i in l:
        element.append(i[::-1])
    return element
words=["abc","tuv","xyz"]
print(reverse_element(words))





 # ["abc","tuv","xyz"]=["cba","vut","zyx"]   lec 100
def reverse_element(l):
    element=[]
    for i in l:
        element.append(i[::-1])
    return element
words=["abc","tuv","xyz"]
print(reverse_element(words))


 # filter odd even [1,2,3,4,5]=[[1,3,5],[2,4]]  lec 101
def filter_odd_even(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output=[odd,even]
    return output
num=[1,2,3,4,5,6,7,8,9]
print(filter_odd_even(num))



# common elemrnt founder function     lec 104
# ip=[1,2,3,4,5]   ,    [1,2,9,8]     op=[1,2]
def common_finder(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output                    # agr ye if k andr chla gya to only 1 aayega isliye position ka dhyan rakho
print(common_finder([1,2,3,4],[1,2,6,7]))

        


# max and min in list     lec 105
num=[1,2,3,4,5,6,7,8]
print(min(num))
print(max(num))

def greatest_diff(l):
    return max(l)-min(l)
print(greatest_diff(num))



#  def a fxn which take ip list in list [1,2,3,[1,2]]     op = list me kitni list he lec 107
def sublistcount(l):
    count=0
    for i in l:
        if type(i)==list:
            count=count+1
    return count
mixlist=[1,2,3,[1,2,3],[4,3,2]]
print(sublistcount(mixlist))