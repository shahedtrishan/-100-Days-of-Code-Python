# print("Welcome to the rollercoaster!")
# height = int(input("What is your height?"))

# if height > 120:
#     print("You can ride the rollercoaster")

# else:
#     print("Sorry! You can't ride the rollercoaster")


# assignment 3.1
# odd_or_even

# 3.0
# number = int(input("Enter the number: "))
# if number % 2 == 0:
#     print("Even Numver")
# else:
#     print("Odd Number")

# 3.1
# nested if

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height?"))
# age = int(input("What's your age?"))

# if height > 120:
#     print("You can ride the rollercoaster")
#     if age <= 12:
#         print("Please pay $30")
#     elif age <= 18:
#         print("Please pay $50")
#     else:
#         print("Please pay $100")
# else:
#     print("Sorry! You can't ride the rollercoaster")

# 3.2
# bmi_calculator_2.0

# height = float(input("enter your height in m: "))
# weight = int(input("enter your height in kg: "))

# BMI = round(weight / height**2)

# if BMI < 18.5:
#     print(f"Your BMI is, {BMI} you are underweight")
# elif BMI < 25:
#     print(f"your BMI is, {BMI} you are normal weight")
# elif BMI < 30:
#     print(f"your BMI is, {BMI} you are slightly overweight")
# elif BMI < 35:
#     print(f"your BMI is, {BMI} you are obese")
# else:
#     print(f"your BMI is, {BMI} you are clinically obese")

# 3.3
# leap_year

# year = int(input("Enter the year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is leap year")
#         else:
#             print(f"{year} is not leap year")
#         print(f"{year} is leap year")
#     else:
#         print(f"{year} is not leap year")
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")

# 3.4
# nested if rollercoaster with pic taken

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height?"))
# age = int(input("What's your age?"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster")
#     if age <= 12:
#         bill = 30
#         print("Please pay $30")
#     elif age <= 18:
#         bill = 50
#         print("Please pay $50")
#     else:
#         bill = 100
#         print("Please pay $100")
#     photo = input("DO you want your photo taken?  Y/N ")
#     if photo == "Y":
#         bill = bill + 5
#     print(f"Your tital bill is ${bill}")
# else:
#     print("Sorry! You can't ride the rollercoaster")


# 3.5
# pizza order practice

# print("Welcome to Trishan's Pizza")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want to add Pepperoni? Y or N ")
# extra_cheese = input("Do you want to add extra cheese? Y or N ")
# bill = 0

# if size == "S":
#     bill = bill + 15
# elif size == "M":
#     bill = bill + 20
# else:
#     bill = bill + 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill = bill + 2
#     else:
#         bill = bill + 3
# if extra_cheese == "Y":
#     bill = bill + 1

# print(f"Your total bill is {bill}")


# 3.7
# love_calculator

print("Welcome to love calculator! ")
name_1 = input("Enter your first name ")
name_2 = input("enter your last name ")
name = name_1 + name_2
lower_case = name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"your score is {score} you are great together")
elif score >= 40 and score <= 50:
    print(f"your score is {score} You are good together")
else:
    print(f"Your score is {score}")
