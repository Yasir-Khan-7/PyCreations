#In this game you have to ask User multiple questions through prompt 
#and the user will answer the questions and you have to calculate total score

QuestionBank = ["what does CPU stands for ",
                "what does RAM stands for ",
                "what does GPU stands for "]

name         = input("What's your name: ").lower()

Answers      =  ["central processing unit",
                "random access memory",
                "general processing unit"]

print(f"Hey! {name.lower()} welcome to the Quiz Game")

score =0
for i in  QuestionBank:
    answer = input(i).lower()
    if answer in Answers:
        print("correct answer")     
        score = score+1         
    else:
        print("wrong answer")
           
          
print(f"your score is {score} and your percentage is {(score/3)*100}")
