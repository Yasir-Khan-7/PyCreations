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
                answer = input("Do you want to enter into the cave? (y/n): ").lower()
                
                if answer =='y':
                    print("Inside the cave, you find two tunnels.")
                    answer = input("Which tunnel will you take? (left/right) ").lower()
                    
                    if answer =='left':
                        print("You encounter a sleeping bear ")
                        answer = input("Do you want to sneak past the bear? (y/n) ").lower()
                        
                        if answer =='y':
                            print("After sneaking past the bear, you reach an underground lake with a small boat")
                            answer = input("Do you want to take the boat across the lake? (y/n)  ").lower()
                            
                            if answer =='y':
                                print("You arrive at a small island in the middle of the lake, where you find an ancient pedestal with an inscription.")
                                answer =input("Do you want to read the inscription? (y/n)  ").lower()
                                
                                if answer =='y':
                                    print("The inscription reads:I can fly without wings. I can cry without eyes. Whenever I go, darkness flies. What am I?" )
                                    answer = input("Answer the riddle (shadow, bird, wind) ")
                                    
                                    if answer == 'shadow':
                                        print("Solving the riddle reveals a hidden passage leading to a treasure chamber")
                                        answer = input("Do you want to enter the treasure chamber? (y/n) ").lower()
                                        
                                        if answer =='y':
                                            print("Inside the treasure chamber, you find a chest filled with gold and jewels, but also a glowing crystal with a mysterious aura.")
                                            answer =input("What will you take? (1: Gold and jewels, 2: Glowing crystal)  ").lower()
                                            if answer =="1":
                                                print("you become wealthy but are haunted by bad luck")
                                                print("The adventure ends here Thank you for playing !...")
                                                break
                                            else:
                                                answer =='2'
                                                print("you gain magical powers and are hailed as a hero")
                                                print("The adventure ends here Thank you for playing !...")
                                                break
                                        else:
                                            answer =='n'
                                            print("you leave the island and the adventure ends")
                                            break
                                    else:
                                        answer =='bird' or answer== 'wind'
                                        print("you answered incorrectly the island starts to sink, and the game ends")    
                                        break
                                else:
                                    answer=='n'
                                    print("you miss a crucial clue and the game ends")
                                    break
                            else:
                                answer =='n'
                                print("you are trapped in the cave and the game ends")
                                break
                        else:
                            answer == 'n'
                            print("the bear wakes up and the game ends")
                            break
                    else:
                        answer == 'right'
                        print("you fall into a deep chasm and the game ends")
                        break
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