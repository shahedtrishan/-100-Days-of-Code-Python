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
