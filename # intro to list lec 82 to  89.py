#  intro to list         lec 82
# orderd collections of iteams, int float string 


numbers=[1,2,3,4]    # numbers list
print(numbers)


words=[ "asd","abcd","shsh"]   
print(words)


mix=[1,2,3,4,"asd","abcd","shsh"]
print(mix)



# acesses the numbers of list

numbers=[1,2,3,4]    # print 1st number =2
print(numbers[1])

words=[ "asd","abcd","shsh"]   # 2nd no.=shsh
print(words[2])


mix=[1,2,3,4,"asd","abcd","shsh"]
print(mix[3])

words=[ "asd","abcd","shsh"]   # 2nd no.=shsh    give list 
print(words[:2])

words=[ "asd","abcd","shsh"]   # 2nd no.=shsh  give list
print(words[:-2])

numbers=[1,2,3,4]    #  change no.
print(numbers[1])

numbers[1]=123      # 1st no.that is 2 will change 123 
print(numbers)


numbers[:1]="123"      # 1st no.that is 2 will change 123 
print(numbers)


numbers[:1]=[1,2,3]      # 1st no.that is 2 will change 123 
print(numbers)

# add data to list   lec 83

name=['sonu','suman','kota']
name.append('1108')            # use to add any new iteam in list
print(name)

# or ek list ko empty rakho or bad me sbkuch iteams dalo

nam=[]
nam.append('sonu')
nam.append('siuman')
nam.append('kota')
print(nam)





#some other method to add list   lec 84
# insert list 
name=['sonu','suman']
name.insert(1,'kota')    # 1 is to give position agr 2 ya 20 lege to hmesha last me aayega 2 se jyada lene pr yha 
print(name)

# join two list 
name=['sonu','suman']
nam=['kota','raj']
name1=name+nam
print(name1)

# extend methd to add
name.extend(nam)     # ye sirf list k element ko le jayega
print(name)
print(nam)


# append method to add  
name.append(nam)    # ye puri list ko le jayega 
print(name)
print(nam)



# methods to delete data from list lec 85
# pop method
name=['sonu','suman','kota','raj']
name.pop()        # pop ,me agr kuch nhi likha to last element ko delete kr dega 
print(name)


name=['sonu','suman','kota','raj']
name.pop(0)        # pop ,me  jo position dalege whi delete hogi
print(name)

name=['sonu','suman','kota','raj']
name.pop(1)         
print(name)

# delete operator
name=['sonu','suman','kota','raj']
del name[1]                         # # del ,me  jo position dalege whi delete hogi    
print(name)


name=['sonu','suman','kota','raj']
del name[0]                         # # del ,me  jo position dalege whi delete hogi    
print(name)

name=['sonu','suman','kota','raj']
del name[ ]                         # # del ,me  agr kuch nhi dala to error    
print(name)


 # remove method 
name=['sonu','suman','kota','raj']
name.remove('kota')
print(name)


name=['sonu','suman','kota','raj']
name.remove('agartala')       #  agr kuch esa remove kiya jo list me nhi he to error aayegi
print(name)



name=['sonu','suman','kota','raj','kota']
name.remove('kota')   # agar koi chij do bar he to remove krne pr phli chij hi remove hogi
print(name)


# in keyword in list lec 86
name=['sonu','suman','kota','raj']
if 'raj' in name:                # koi iteam list me he ya nhi check krne k liye 
    print(' is prenent')
else:
        print('not present')




# some more list methods  lec 87
name=['sonu','suman','kota','sonu','raj','sonu']
print(name.count('sonu'))                   # count the iteam in list



# for alphabetical sorting
name.sort()     # for alphabetical sorting
print(name)        # can't use print(name.sort())

# sorting of number can also be done
num=[1,2,1,4,3,8,7,6,4,3,0]
num.sort()                         # yha list asli me sortb ho rhi he mtlb ab agr waps print krayege to sorted aayegi 
print(num)


# sorted function
num=[1,2,1,4,3,8,7,6,4,3,0]
print(sorted(num))                # isme list sort nhi ho rhi only sorted order me print ho rhi he 
print(num)                                 # mtlb agr waps print krayege to sorted nhi aayegi


# clear to clear list
num=[1,2,1,4,3,8,7,6,4,3,0]
num.clear()
print(num)



# copy of numbers
num=[1,2,1,4,3,8,7,6,4,3,0]
numcopy=num.copy()
print(numcopy)



# is v\s == in python    lec 88
# list comparision use == and is key word
name1=['sonu','suman','kota']
name2=['sonu','suman','raj']
name3=['sonu','suman','kota']
print(name1==name2)
print(name1==name3)      # value same
print(name3==name2)


name1=['sonu','suman','kota']
name2=['sonu','suman','raj']
name3=['sonu','suman','kota']
print(name1 is name3)      # value same  but address alg he alg memory location pr he is liye name 1 and name 2 alg alg object he 





# split and join method 
# split convert string in list
name='sonu suman kota raj'.split()   # jha jha space hoga wha se tod k list bna dega 
print(name)


# yha space nhi lekr coma lerha hu todne k liye to split me bhi koma aayega 
name='sonu,suman,kota,raj'.split(',')   # jha jha space hoga wha se tod k list bna dega 
print(name)



# alg alg variable me store kra skte he 
name,surname,city,state='sonu,suman,kota,raj'.split(',') 
print(name)
print(surname)
print(city)
print(state)




 
# user se input krane k liye 
name,surname,city,age=input('enter your information').split(',')   # yha number ko lene k liye string lena jruri nhi he 
print(name)
print(surname)
print(city)
print(age)




# join convert list to string 
name=["sonu",'suman',"25"]     # yha sbhi number or word ko string me lena pdega int me liya to error
print(",".join(name))