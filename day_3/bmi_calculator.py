# 3.2
# bmi_calculator_2.0

height = float(input("enter your height in m: "))
weight = int(input("enter your height in kg: "))

BMI = round(weight / height**2)

if BMI < 18.5:
    print(f"Your BMI is, {BMI} you are underweight")
elif BMI < 25:
    print(f"your BMI is, {BMI} you are normal weight")
elif BMI < 30:
    print(f"your BMI is, {BMI} you are slightly overweight")
elif BMI < 35:
    print(f"your BMI is, {BMI} you are obese")
else:
    print(f"your BMI is, {BMI} you are clinically obese")
