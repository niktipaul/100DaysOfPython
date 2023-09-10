# PROJECT 5

# PASSWORD GENERATOR


import random

print('WELCOME TO PASSWORD GENERATOR')

much_letters = int(input('How many letters would you like in yoiur password?\n'))
much_symbols = int(input('How many symbols would you like?\n'))
much_numbers = int(input('How many numbers would you like?\n'))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
           'C', 'D', 'E', 'F', 'G', 'HI', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!','@','#','$','%','^','&','(',')','*','+']
numbers = ['1','2','3','4','5','6','7','8','9','0']

password = []
for i in range(much_letters):
    password += random.choice(letters)

for i in range(much_numbers):
    password += random.choice(numbers)

for i in range(much_symbols ):
    password += random.choice(symbols)

random.shuffle(password)
print('Here is your password',''.join(password)) 