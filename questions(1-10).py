#below are the questions 1-10 from Practice Python


#write a program that takes the sum of all positive numbers


numbers = [34, -5, 67, -2, 89, -1, 0, 23]
def sum_positive_numbers(numbers):

    total = 0 
    for num in numbers:
        if num > 0:
            total = total + num 

    return total

# result =sum_positive_numbers(numbers)

# print("The sum of all the positive numbers is: ", result )

#create a functions that takes a sentence and count the total number of words in it 

 
# sentence = input("Enter a sentence: ")

def count_words(sentence):

    words = sentence.split(" ")
    num_words = len(words)

    return num_words

# word_count = count_words(sentence)
# print("The total number of words in sentence is : ", word_count)


#question create a program that is responsible to swap two variables


# value1 = input("Enter the first number:  ")

# value2  = input("Enter the second number:  ")

def swap_variables(x,z):


    temp = x
    x=z 
    z= temp 
    return x,z

# val1,val2 = swap_variables(value1,value2)
# print("After swapping the values are: ", val1, val2)
