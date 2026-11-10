# dictionaries : are store in key valude pair .

band = {
    "vocal": "plant",
    "guitar" : "page"
}


band2 = dict( vocal="plant",guitar = "page")
band2 = dict( vocal="plant")

print(band)
print(band2)
print(type(band))
print(len(band))

# Acess items
print(band["vocal"])
print(band.get("guitar"))

# list all keys // like key of the values
print(band.keys())

# //list all values 
print(band.values())

# list of all key value pair as tuple
print(band.items())
# verify a key esixt 
print("guitar" in band)
print("triangle " in band)

# change values 
band["vocal"] = "coverdale"
band.update({"bass": "jpj"})

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "bonham"
print(band)

print(band.popitem())  # tuple:
print(band)

# delete and clear
band["drums"] = "bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# # copy dictionary 
# # not good coppy
band2 = band # creta a refrence
print("Bad copy !")
print(band2)
print(band)

band2["drums"] = "Dave"
print(band)

# how to crate a copy 
band2 = band.copy()
band2["drums"] = "Dave"
print("Good Copy!")
print(band)
print(band2)

# or use the dictionat() cont funtion 
band3 = dict(band)
print("good Copy!")
print(band3)

# Nestes Dictionaries 
member1 = {
    "name" : "plant",
    "instument" :"voacals"
}

member2 = {
    "name" : "plant",
    "instrument" : "guitar"
}

band = {
    "member1" : member1,
    "member2" : member2
}

print(band)
print(band["member1"]["name"])

# sets is data collection type

num = {1,2,3,4,5}
num2 = set((1,2,3,4,5))
print(num)
print(num2)
print(type(num2))
print(len(num))

# No duplicate are allowed in set
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2 , False , 3 , 4, 0}
print(nums)

# check if a vlaue is  a set 
print(2 in nums)

# but you cannot refer to an element in the set with
#  an index position or a key 

# but you can not refer to an element in the set with
# and index postion or a key

# add a new eleent to a set
num.add(8)
print(nums)

# add element from one set to anothers 
more_nums = {5,6,7}
nums.update(more_nums)
print(nums)

# you can use update with lst , tuples, and dictionares too.

# Merge two set to crate a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates 
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)
  
