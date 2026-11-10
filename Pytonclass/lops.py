# while loop execute the block of code if the condition is true.
# value = 1 
# while value <= 10: 
#     print(value)
#     if value == 5:
#        # break
#     value += 1


# value = 1 
# while value <= 10: 
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("value is now equal to 10" + str(value))

    # for loop 
# names = ["neil", "dave", "james", "john"]

# for name in names:
#     print(name)

# for name in names:
#     if name == "james":
#         break
#     print(name)

# for name in names:
#     if name == "james":
#         continue
#     print(name)


#ranges
# for x in range(5):
#     print(x) 

#ranges
# for x in range(2,4):
#     print(x) 

# for x in range(5, 100, 5):
# for x in range(5, 101, 5):
#     print(x) 
# else:
#     print("done")

names = ["neil", "dave", "james", "john"]
actions = ["code ", "eats", "sleeps" "play"]

for action in actions:
    for name in names:
        print(name + " " + action + " ." )