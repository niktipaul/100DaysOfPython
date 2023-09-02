# CLASS NOTES 2: Type Error, Type Checking and Type Conversion

# len(1234)
# TypeError: object of type 'int' has no len()

name_char = len(input("What is your Name? "))
print(type(name_char))          # Type checking of Variables

new_name_char = str(name_char)  # Type conversion
print(type(new_name_char))   
print("Your name has " +  new_name_char + " characters")


# TYPE CONVERSION

print(70 + float("100.25"))
print(str(70) + str(100))

