#Password Generator Project
#import the random module
import random

#Create lists of potential pw characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
#Collect information criteria from user
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Begin with empty list
password = []

#Make random selections using the amounts collected from questioning
random_numbers = (random.choices(letters, k=nr_letters))
random_letters = (random.choices(numbers, k=nr_numbers))
random_symbols = (random.choices(symbols, k=nr_symbols))

#Concatenate the lists
password = random_numbers + random_letters + random_symbols
#shuffle the concatenated list
random.shuffle(password)
#create new empty string for password variable
newpw = ""
#for each character in the list (after shuffle) add to new password variable (newpw) one character at a time
for character in password:
    newpw += '' + character
print(newpw)

