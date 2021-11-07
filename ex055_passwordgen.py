# Password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))

password = ""

# Generate the random characters for each type for the given password length

for char in range (1,nr_letters + 1):
    password += random.choice(letters)
    print(password)

for char in range(1,nr_symbols + 1):
    password += random.choice(symbols)
    print(password)

for char in range(1,nr_numbers + 1):
    password += random.choice(symbols)
    print(password)

# Randomizes the order of the character types and displays password as string
    
password = list(password)
password_shuffled = random.shuffle(password)
print(password)
password_as_string = ""
print(password_as_string.join(password))