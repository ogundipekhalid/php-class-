# meani = 5
# print('')

# if meani > 10:
#     print('rig on')
# else:
#     print('not tod')    
    
    # tenary operator
# print('rig  on') if meani > 10 else print('not 2d')

# leseson 4
# data types
# string datatypes 

# literal assignment 
first = "dave"
last = "gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first , str))

# construction funtion
# pizza = str(5) 
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza , str))

# concatination
fullanme = first + "" + last 
print(fullanme)
fullanme += "!"
print(fullanme)

# casting a number to string
decade = str(1900)
print(type(decade))
print(decade)

statement  = "i like music " + decade + "s."
print(statement)

# mutiple line 
multiline = '''
hey yo       

i was just       

            all good

'''
print(multiline)

# Escaping Special characters 
sentanecs = 'I\'m back at it ! \they\n \n where\'s this at\\loc'
print(sentanecs)


# string method
print(first)
print(first.lower())
print(first.upper())
# print(first.lower())


print(multiline.title())
print(multiline.replace("good job" ,"ok"))
print(multiline)
print(len(multiline))
multiline += multiline
multiline  = "  " + multiline
print(len(multiline))
print(len(multiline))
# remove the white space 
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# othere strings method in onlie rad for that 
print("")
# build a menu
title = "menu".upper()
print(title.center(20, "="))
print("coffe".ljust(16,".")+ "$1".rjust(4))
print("muffin".ljust(16,".")+ "$3".rjust(4))
print("cheasecake".ljust(16,".")+ "$5".rjust(4))
print("")

# stringe index value 
print(first[1])
print(first[-1])
# renage value
print(first[1: -1])
print(first[1:])
# some method return boolean data
print(first.startswith("d"))
print(first.endswith("Z"))
# boolean data types 
myvale = True
x = bool(False)
print(type(x))
print(isinstance(myvale,bool))

# numeric datatypes 
# integer type 
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price,int))
# float type
gpa = 4.51
y= float(1.12)
print(type(gpa))

# complex type
comp_valuue = 5 + 3j
print(type(comp_valuue))
print(comp_valuue.real)
print(comp_valuue.imag)
# built-in funtions for numbers 
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

# math mdules uses liberies like extention
import math 
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to number
zipcode = "10011"
zip_value = int(zipcode)
print(type(zip_value))

# Error if attempt to cast incorrect data
# Zip_Value = int("New york")

