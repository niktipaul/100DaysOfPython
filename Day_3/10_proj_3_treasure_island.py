# PROJECT 3: TREASURE ISLAND

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')

print('\nWelcome to Treasure Island.\nYour mission is to find treasure')
left_right = input('You\'re at a cross road.Where do you want to go? "left" or "right"\n')

if left_right == 'left':
    swim_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    
    if swim_wait == 'wait':
        which_door = input('You arrive at island unharmed. There is a house with 3 doors. One red, one blue and one yellow. Which color do you choose?\n')

        if which_door == 'red':
            print('Burned by fire, GAME OVER!!!')
        elif which_door == 'blue':
            print('Eated by beasts, GAME OVER!!!')
        elif which_door == 'yellow':
            print('You got the treasure, YOU WIN!!!')
        else:
            print('GAME OVER!!!')

    else:
        print('Attacked by trout, GAME OVER!!!')
        

else:
    print("Fall into a hole, GAME OVER!!!")
