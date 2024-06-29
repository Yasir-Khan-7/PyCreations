#in this Game the user will guess the number and will be checked against the random number generated
import random

number = input("Enter a number: ")

if number.isdigit():
    range_of_number = int(number)
    if range_of_number > 0:
        quit()
    elif range_of_number<=0:
        print("please enter a number greater than 0")
        quit()
else:
    print("please enter a number ")    
    
#now going towards guessing
random_no = random.randrange(0,number)
print(random_no)
       
