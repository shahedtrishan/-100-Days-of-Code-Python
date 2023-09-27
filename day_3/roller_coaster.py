# 3.4
# nested if rollercoaster with pic taken

print("Welcome to the rollercoaster!")
height = int(input("What is your height?"))
age = int(input("What's your age?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        bill = 30
        print("Please pay $30")
    elif age <= 18:
        bill = 50
        print("Please pay $50")
    else:
        bill = 100
        print("Please pay $100")
    photo = input("DO you want your photo taken?  Y/N ")
    if photo == "Y":
        bill = bill + 5
    print(f"Your tital bill is ${bill}")
else:
    print("Sorry! You can't ride the rollercoaster")
