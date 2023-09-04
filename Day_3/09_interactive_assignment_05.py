# INTERACTIVE ASSIGNMENT 5

# 💪 This is a Difficult Challenge 💪

# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"

# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times

# Total = 3
# Love Score = 53

# Print: "Your score is 53."

# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.

# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
# Example Output 2
# Your score is 73.

print('Welcome to Love Calculator!')
name_1 = input('What is your name? ')
name_2 = input('What is their name? ')

true_count = 0
love_count = 0

mixed_name = name_1 + name_2
mixed_name = mixed_name.upper()

true_count += mixed_name.count('T')
true_count += mixed_name.count('R')
true_count += mixed_name.count('U')
true_count += mixed_name.count('E')

love_count += mixed_name.count('L')
love_count += mixed_name.count('O')
love_count += mixed_name.count('V')
love_count += mixed_name.count('E')

final_score = true_count * 10 + love_count

if final_score < 10 or final_score > 90:
    print(f'Your score is {final_score}, you go together like coke and mentos.')
elif final_score >= 40 and final_score <= 50:
    print(f'Your score is {final_score}, you are alright together.')
else:
    print(f'Your score is {final_score}')

