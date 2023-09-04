# INTERACTIVE ASSIGNMENT 2

# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as
# names followed by comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

import random

print('Welcome to Bankers Roulette')
names = input("Give me everybody's names seperated by a comma(,):\n")
name_list = names.split(',')

bill_payer_index = random.randint(0,len(name_list)-1)
print(f"{name_list[bill_payer_index]} is going to pay today's bill.")