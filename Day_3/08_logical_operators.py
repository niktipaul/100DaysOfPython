# NOTES 4: Logical Operators

# Giving free tickets to people with midlife crisis

print('Welcome to the Rollercoaster')
height = int(input('What is your height in cms? '))
bill = 0

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))

    if age < 12:
        print('Child tickets are ₹50')
        bill += 50

    elif age <= 18:
        print('Youth tickets are ₹70.')
        bill += 70

    elif age >= 45 and age <= 55:
        print('Everything is gonna be okay, enjoy a free ride on us!')

    else:
        print('Adult tickets are ₹120.')
        bill += 120
    
    photo = input('Do you want a photo taken? Y or N. ')
    if photo == 'Y':
        bill += 30
    
    print(f'Your final bill is ₹{bill}.')

else:
    print('Sorry, you have to grow taller before you can ride.')