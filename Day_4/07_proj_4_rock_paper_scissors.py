# PROJECT 4

# ROCK PAPER SCISSORS

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


symbols = [rock,paper,scissors]

your_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))

if your_choice < 0 or your_choice > 2:
    print('Invalid choice!!!')
    exit()

print('You Choice:-')
print(symbols[your_choice])

computers_choice = random.randint(0,2)
print("\n\nComputer's Choice:-")
print(symbols[computers_choice])

if your_choice == computers_choice:
    print('Game Tied!!!, try Again!!!')

elif your_choice == 0 and computers_choice == 2:
    print('Hurray!!!, You Won!!!')

elif your_choice == 1 and computers_choice == 0:
    print('Hurray!!!, You Won!!!')

elif your_choice == 2 and computers_choice == 1:
    print('Hurray!!!, You Wonn!!!')

else:
    print('Soory, You Lost!!!')