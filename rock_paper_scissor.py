#This is rock , paper , scissor game user vs computer
#now lets first know what we have to do in it
# take user input and take a random number compare both if user is winning increase counter

import random
options = ['rock','paper','scissor']
user_won = 0
computer_won = 0
while True:
    user_input = input("Enter rock/paper/scissor or q to start or quit game: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    randomnumber= random.randint(0,2)
    # rock :0 , paper:1 scissor:2
    computer_pick = options[randomnumber]
    if user_input =="rock" and   computer_pick =='scissor':
        print("you won!")
        user_won +=1
    elif user_input =="scissor" and   computer_pick =='paper':
        print("you won!")
        user_won +=1
    elif user_input =="paper" and   computer_pick =='rock':
        print("you won!")
        user_won +=1
    else:
        print("computer won!")
        computer_won+=1

print("goodbye!\n")
print("user won times:\n ",user_won)
print("computer won times: ",computer_won)