# PROJECT 2

# TIP CALCULATOR

print('Welcome to tip calculator.')
total_bill = float(input('What was the total bill?  ₹'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

print(f"Each person should pay: ₹{round((total_bill*(1+tip_percentage/100)) / people, 2)}")