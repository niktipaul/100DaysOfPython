# INTERACTIVE ASSIGNMENT 4

# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"

# Example Output
# Your final bill is: $28.

print('Welcome to Python Pizza Deliveries!')
size_of_pizza = input('What size of pizza do you want? S, M or L?  ')
want_pepperoni = input('Do you want pepperoni? ')
want_cheese = input('Do you want cheese? ')

bill = 0

if size_of_pizza == 'S':
    bill += 150

elif size_of_pizza == 'M':
    bill += 200

elif size_of_pizza == 'L':
    bill += 250

else:
    print('Invalid Choice!!!')
    exit()

if want_pepperoni == 'Y':
    if size_of_pizza == 'S':
        bill += 20
    else:
        bill += 30

if want_cheese == 'Y':
    bill += 10

print(f"Your final bill is ₹{bill}")

