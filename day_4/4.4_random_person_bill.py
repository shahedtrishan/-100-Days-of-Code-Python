# randomize who is going to pay the bill

import random

names_string = input("give me names separated by comma. ")
names = names_string.split(", ")
random_choice = random.choice(names)
print(random_choice)
