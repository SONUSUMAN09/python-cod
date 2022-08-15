# list me data achche se represent nhi kr skte isliye hm dictionaries use krte he like
# sonu=[name,age,[a,b,c],[q,w,e]]- ese achche se sbhi info nhi represent nhi hoti to 
# dictionaries me data represent krte he -
# unorderd collection of data in key : value pair
# create dictionaries
user={'name' : 'sonu', 'age' : 24}  # name = key   sonu = value pair
print(user)
print(type(user))

#second method to create dictionaries
user1=dict(name='sonu', age=24)           # difference dikh rha hoge 2nd me string k liye '' lene ki jrurt nhi he
print(user1)

# acess data in dictionary- inme indexing nhi hoti list ki trh
user={'name' : 'sonu', 'age' : 24} 
print(user[0])     # error dega 
print(user['name'])    # ye key se access krta he data ko
print(user['age'])

# any type data can be stored in dictionaries
user={
    'name':'sonu',
    'age':24,
    'animal':['kutta','billi'],
    'vehical':['car','bike'],
}
print(user)
print(user['animal'])



# dictionary in dictionary
user={
    'user':{'name' : 'sonu', 'age' : 24} ,
    'name':'sonu',
    'age':24,
    'animal':['kutta','billi'],
    'vehical':['car','bike'],
}
print(user)
print(user['animal'])


# add data to empty dictionary
user={}
user['name']='sonu'
user['age']=24
print(user)