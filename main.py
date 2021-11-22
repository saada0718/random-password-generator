#Import the random library
import random

#initialize the variables
upper_case = False
special_character = False
number = False

#The password length in 8 by default
length = 8

#You either have to include an upper case character and/or a special character and/or number.
round = False
while not(upper_case or special_character or number):
    if round:
      print("You need to include one of the following in your passowrd\n\t- An upper-case letter\n\t- A special character\n\t- A number")
    if input("Does your Password contain an upper case letter? (y/n) ").lower() == "y":
        upper_case = True

    if input("Does your password contain a special character? (y/n) ").lower() == "y":
        special_character = True
    
    if input("Does your password contain a number? (y/n) ").lower() == "y":
        number = True
    round = True
#Ask the user for the length of the password
temp = input("Please type in the length that you would like your password to be? ")
#Keeps looping until the input is a number and the length of the password is atleast four characters
while True:
    if not(temp.isdigit()):
        temp = input("Your input was not a number please try again ")
    elif int(temp)<4:
        temp = input("The minimum length is supposed to be at least 4 characters ")
    else:
        break
length = int(temp)
#Due to the ascii values of the special characters not being consequtive, I stored them in an array so that I can get a value randomly from it
spec_chr = [chr(i) for i in range(32, 48) ] + [chr(j) for j in range(58,65)] + [chr(k) for k in range(123,127)]
#Declare an array with null value that is of length stated by the user
#This will store the password in char values
password  = [None] * length

"""
Given the instructions stated by the user this gets a random value with that specification and stores it in a random spot in the array 
and then sets the boolean to false so that we don't have to put a value with that specification in the password again.
"""
while None in password:
    if upper_case:
        letter = random.randint(65,90)
        location = random.randint(0,length-1)
        if password[location] == None:
            password[location] = chr(letter)
            upper_case = False
            
    if special_character:
        letter = spec_chr[random.randint(0,len(spec_chr)-1)]
        location = random.randint(0,length-1)
        if password[location] == None:
            password[location] = letter
            special_character = False
    if number:
        letter = random.randint(48,57)
        location = random.randint(0,length-1)
        if password[location] == None:
            password[location] = chr(letter)
            number = False
    """
    If the password contains a number, a special character and an upper case character (If the user asked for these) and there is still space then 
    the rest of the password will contain lower case letters.    
    """
    if not(number) and not(special_character) and not(upper_case):
        letter = random.randint(97,122)
        location = random.randint(0,length-1)
        if password[location] == None:
            password[location] = chr(letter)
#Declaring a string that will get all the char values from the array to store as a string
finalPassword = ""
#Taking all the char values from the array and storing them in a string
for letter in password:
    finalPassword += letter
#Providing the user with the string   
print("Your password is:",finalPassword)
