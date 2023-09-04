# NOTES 3: IndexErrors and working with nested lists



# INDEX ERRORS

states_of_india = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
                   "Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
                   "Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
                   "Uttarakhand","West Bengal"]

print(len(states_of_india)) # 28

print(states_of_india[28])
# IndexError: list index out of range

print(states_of_india[len(states_of_india)])
# IndexError: list index out of range

print(states_of_india[len(states_of_india)-1])
# # West Bengal



# NESTED LIST

dirty_dozens = ['Strawberries','Spinach','Kale','Nectarines','Apples','Grapes','Peaches','Cherries','Pears','Tomatoes','Celery','Potatoes']

fruits = ['Strawberries','Nectarines','Apples','Grapes','Peaches','Cherries','Pears']
vegetables = ['Spinach','Kale','Tomatoes','Celery','Potatoes']

dirty_dozens_v2 = [fruits, vegetables]  # Nested List
print(dirty_dozens_v2)