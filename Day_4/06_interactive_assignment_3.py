# INTERACTIVE ASSIGNMENT 3

# Treasure Map

treasure_map = [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
print(f"{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}\n")
axis_ = int(input('Where do you want to put the treasure?  '))

row = (axis_ % 10) - 1
column = (axis_ // 10) - 1

if row < len(treasure_map) and column < len(treasure_map[row]):
    treasure_map[row][column] = ' X'
    print(f"{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}\n")

else:
    print('Invalid position to place trasure!!!.')