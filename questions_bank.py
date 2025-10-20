#below are questions 11-20 from the Practice python




#Variable and Data Types

#given a list of numbers, find the sum and  average 

# num_list = [12,3,4,5,6,7]


def sum_and_average(num_list):
    sum_number = 0
    average = 0
    for num in num_list:

        sum_number = sum_number + num

    average = sum_number / len(num_list)


    return sum_number, average


# sum,average = sum_and_average(num_list)
# print(f"the sum is : {sum} and the average is : {average}  ")



#given a list of names and concatenate them into single sentence with spaces

lst_str = ["yasir","is"," a","good"]

def concatenate_names(lst_str):


        sentence = " ".join(lst_str)
        return sentence
    

result = concatenate_names(lst_str)



#Loops and control statements

#write a program to print the table of a given number


# user_input = input("enter a number to print its table:  ")

def table_of_number(user_input):
     

     for x in range(user_input):
          

          print( f"{user_input} x {x+1} = {user_input * (x+1)}"  )


# table_of_number(int(user_input))


#write a program to calculate the factorial of a given number


# user_input = int(input("enter a number to find its factorial:  "))

def factorial_of_number(n):
  
 
         
        if n==1 or n==0:
            return 1
        else:
            return (n * factorial_of_number(n-1))
    

# result = factorial_of_number(user_input)
# print(f"The factorial of {user_input} is : {result} ")


 #return all prime numbers between the 1 to 50 



def prime_numbers():
    primes = []

    for x in range(1,51):
         if x >1 and x %2 !=0:
              primes.append(x)

    return primes

result = prime_numbers()
print("The prime numbers between 1 to 50 are: ", result)





#numpy and pandas exercises and matplotlib total = 30

