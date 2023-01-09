import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")


# num_items = len(names)

# random_choice = random.randint(0, num_items - 1)

person_who_will_pay = random.choice(names) #This code is the easiest way 

print(person_who_will_pay + " is going to buy meal for today")
