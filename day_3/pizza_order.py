# 3.5
# pizza order practice

print("Welcome to Trishan's Pizza")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want to add Pepperoni? Y or N ")
extra_cheese = input("Do you want to add extra cheese? Y or N ")
bill = 0

if size == "S":
    bill = bill + 15
elif size == "M":
    bill = bill + 20
else:
    bill = bill + 25

if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3
if extra_cheese == "Y":
    bill = bill + 1

print(f"Your total bill is {bill}")
