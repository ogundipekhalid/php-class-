# 
user = ['dave', 'jhone', 'sara']
data = ['dave', 43 , True]
emptylist = []
print("dave" in emptylist)
# print("dave" in user)
print(user[0])
print(user[-2])
print(user[2])
print(user.index('sara'))
print(user[0:2])
print(user[1:])
print(user[-3:-1])
print(len(data))
# use to add new stings in list     
user.append('elsa')
print(user)
user += ['jason']
print(user)
user.extend(['robert', 'jimmy'])
print(user)
# user.extend(data)
# print(user)
user.insert(0,'bob')
print(user)
user[2:2] = ['eddie', 'alex']
print(user)

user[1:3] = ['robert', 'jp']
print(user) 
# to remove 
user.remove('bob')
print(user)
#  to pup out the last on the list 
print(user.pop())
print(user)

del user[0]
print(user)


# del data
data.clear()
print(data)

user[1:2] = ['Dave']
user.sort()
print(user)

user.sort(key=str.lower)
print(user)

num = [4 ,42,78, 1,5]
num.reverse()
print(num)
# ///  
# num.sort(reverse=True)
# print(num)

# gloalal  sorted fruntoin 
print(sorted(num , reverse=True))
print(num)

numscopy = num.copy()
mynums = list(num)
mycopy = num[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(num)

print(type(num))

mylist = list([1, "neil", True])
print(mylist)

# //Tuple // can not be change 
mytuple = tuple(('Dave', 42, True))

anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# but add  new list tuple by geting cretative 
newlist =  list(mytuple)
newlist.append('nieal')
newtuple = tuple(newlist)
print(newtuple)

# unpacking tuple puting values in this varable name 
(one , *two,  hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))

