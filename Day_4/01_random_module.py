# NOTES 1: Random Module (Pseudorandom number generators)

# Python Random use logic based on Mathematics Mersenne Twister
# TIP: askpython.com to search modules and get documentation.

import random

random_integer = random.randint(1, 10) #inluding 1 and 10
print(random_integer)


random_float = random.random()
print(random_float)


# Random decimal numbers between 0 and 5
random_dec = random.random() * 5
print(random_dec)

love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')