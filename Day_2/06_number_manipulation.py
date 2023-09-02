# CLASS NOTES 4: Number Manipulation anf fString


# Example 1: 
print(8 / 3) 
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))
print(8 // 3)

# Example 2:
result = 4 / 2
result /= 2
print(result)

# Example 3:
score = 0
score += 1      # score = score + 1
print(score)

# Usinf fstrings

score = 0
height = 1.8
isWinning  =True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")