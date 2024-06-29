#in this Game the user will guess the number and will be checked against the random number generated
#note: break terminates the loop completely and continue terminates the current iteration 
import random

def Number_guesser(range_of_no,random_no):
    guesses = 0

    print(f"random number was: {random_no}")
    
    while True:
        number = input("Enter number to Guess: ")
        guesses=guesses+1
        if random_no==int(number):
            print(f"you got it in {guesses}")
            exit()
        else:  
            print("try again")
            continue
         
range_of_no =6
random_no = random.randint(1,range_of_no)       
Number_guesser(range_of_no,random_no)