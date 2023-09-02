# INTERACTIVE ASSIGNMENT 4

# Instructions
# Write a program that switches the values stored in the variables a and b.

# Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.

# Example Input
# a: 3
# b: 5
# Example Output
# a: 5
# b: 3


# SOLUTION

a = input("a: ")
b = input("b: ")

a,b = b,a

# another solution
# c = a
# a = b
# b = c

print('a:',a)
print('b:',b)