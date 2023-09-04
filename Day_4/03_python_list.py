# NOTES 2: Understanding the offset and appending items to lists

states_of_india = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
                   "Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
                   "Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
                   "Uttarakhand","West Bengal"]

print(len(states_of_india))
print(states_of_india[0])
print(states_of_india[-1])

states_of_india.append('<Some new state>')
print(states_of_india)

states_of_india.pop()
print(states_of_india)