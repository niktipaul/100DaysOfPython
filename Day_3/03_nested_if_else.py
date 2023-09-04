# NOTES 2: Nested if statement and elif statement

print('Welcome to the Rollercoaster')
height = int(input('What is your height in cms? '))

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))
    if age < 12:
        print('Please pay ₹50')
    elif age <= 18:
        print('Please pay ₹70.')
    else:
        print('Please pay ₹120.')
else:
    print('Sorry, you have to grow taller before you can ride.')
