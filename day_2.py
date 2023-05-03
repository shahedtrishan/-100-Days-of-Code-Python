# day_2
fname = input("whats your fname?\n")
lname = input("Whats your lmane?\n")

print("Your fullname is: " + fname + " " + lname)
length = len(fname+lname)
print("your name length is: " + str(length))


# data type

num = 1234
print(type(num))

floatttttt =  12.12
print(type(floatttttt))

# day2 exercise 1 challange

digit = input("Enter two digits:\n")
print("" + int(digit[0]) + int(digit[1]))

# or


two_digit_number = input("Type a two digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)

print(result)

# challange_2 bmi_calculator


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
full_num= int(bmi)

print(full_num)

# Exercise 3 - Life in Weeks

age = input("What is your current age? ")

years = 90 - int(age)
days = years * 365
weeks = years * 52
months = years * 12 

print("you have " + str(days) + " days, " + str(weeks) + " weeks, " + str(months) + " months left.")
finala = f"You have {days} days, {weeks} weeks, and {months} months left."

print(finala)



#day two final project tip calculator

print("Calculate your tip!")
bill = float(input("total bill? $ "))
tip = int(input("How much tip? "))
people = int(input("Total People? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(final_amount)
