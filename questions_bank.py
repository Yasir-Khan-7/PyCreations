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

# result = prime_numbers()
# print("The prime numbers between 1 to 50 are: ", result)





#numpy and pandas exercises and matplotlib total = 30

#create a numpy array and do basic multiplication and addition 

import numpy as np 

mylist = [1,2,3,4,5]
mylist2 = [13,14,15,16,17]
numarray = np.array(mylist)
numarray2 = np.array(mylist2)

#addition of numpy array
# print(numarray+numarray2)


#Create a numpy array and calculate its  mean ,median mode and standard deviation

arr = np.array([3,4,5,6])

meanres = arr.mean()
medres = np.median(arr)

stdres = arr.std()
# print(meanres)
# print(medres)
# print(stdres)


#create a numpy array and create it into different shapes 


shapearr = np.array([1,2,3,4,5,6])

checkshape = shapearr.shape

# print(checkshape)

updateshape = shapearr.reshape(3,2)

# print(updateshape)



#Q1 to 10 numpy --> 


#Question 1 
# create a numpy arraay from the python list and do something on it perform multiplications or anythin

lst = [1,2,3,4,6]

arr = np.array(lst)

arr2 = np.array(lst)
# print(arr.sum())
# print(np.multiply(arr,arr2))



#Question 2 
#a program that genrerates a numpy array from 0 to 9 and then reshape it into 3X3

def manipulation():
    myls = []
    for x in range(9):
        print(x)
        myls.append(x)
      
    req= np.array(myls)    
    print(req.reshape(3,3))

# manipulation()

#create a function tthat takes numpy array and sort in ascending order 


lstas = [2,4,1,5,8,7,6,9]
def sortasc(arr):
    newarr = np.array(arr)
            
    return np.sort(newarr)   

result =sortasc(lstas)  
print(result)  
