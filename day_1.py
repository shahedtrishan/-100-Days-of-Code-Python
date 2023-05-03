# day 1 exercise 1

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#exercise 2 debudding

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Exercise 3 - Input Function

user = input("What is your name? ")
length = len(user)
print(length)
print(len(input("What is your name? ")))

# Exercise 4 - Variables

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

# Day 1 Project: Band Name Generator

print("Hello create your band name here")
city = input("Name of the city?\n")
pet = input("Name of the pet?\n")
print(city + " " + pet)