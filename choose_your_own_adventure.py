#This is adventure game where user  will enter into an adventure and explore crazy things and places
name = input("Enter your name:  ")
print(f"{name} Welcome you to the  'LOST TREASURE'  you have an old map that leads to  a hidden treasure in a forest: ")

while True:
    answer = input("Do you want to enter into the adventure: (y/n) ").lower()
    if answer =='y':
        print("Yeah! so here you go choose wisely ")
        answer  = input("Which path will you take left or right: ").lower()
        
        if answer == 'left':
            print("You encounter a river with a rickety bridge.")

            answer = input("Do you want to cross the bridge? (y/n) ").lower()
            
            if answer =='y':
                print("You see a cave entrance hidden behind some bushes.")
                answer = input("Do you want to enter into the cave? (y/n): ")
                
                if answer=='y':
                    print("Inside the cave, you find two tunnels.")
                else:
                    answer =='n'
                    print("your adventure ends here goodbye :)")
                    break
        else:
            answer == 'right'
            print("you fall into a hidden pit and the game ends.")
            break
   
    elif answer =='n':
        print("your adventure ends here :) good bye! ")
        break
    else:
        print("please enter 'y' to enter into adventure or 'n' to  end the adventure! ")
        continue