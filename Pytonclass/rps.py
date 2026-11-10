import sys
import random
from enum import Enum

# libariy for enum
class RPS(Enum):
    ROCK = 1 
    PAPER = 2
    SCISSORS = 3



# roke pepper scissors
# value = input('place enter a value\n')
# print(value)
print("")

playerschoice = input("enter...\n1 for rock , \n2 for paper,or \n3 for scissors : \n\n")
# typcate here 
player = int(playerschoice)
# if playerschoice < 1 or playerschoice > 3
if player < 1 or player > 3: 
    sys.exit("you must enter 1, 2, or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)


print("")
print("you chose" + str(RPS(player)).replace('RPS.','') + ".")
print("python chose" + str(RPS(computer)).replace('RPS','') + ".")
print("")
# now statement
if player == 1 and computer == 3:
    print("😊🏅you win!")
elif player == 2 and computer == 1:
    print("😊🏅you win!")
elif player == 3 and computer == 2:
    print("😊🏅you win!")
elif player == computer:
    print("🤷‍♂️tie game!")
else:
    print('🐍python wins!')



# 
# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()