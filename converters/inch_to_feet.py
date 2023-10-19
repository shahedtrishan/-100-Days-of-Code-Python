# Function to convert inches to feet
def inch_to_feet(inch):
    feet = inch / 12
    return feet


# Function to convert centimeters to feet
def cm_to_feet(cm):
    feet = cm / 30.48
    return feet


while True:
    # Prompt the user to choose the conversion type
    print("Choose the conversion type:")
    print("1. Inches to Feet")
    print("2. Centimeters to Feet")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        inch_length = float(input("Enter a length in inches: "))
        feet_length = inch_to_feet(inch_length)
        print(f"{inch_length} inches is equal to {feet_length:.2f} feet")
    elif choice == 2:
        cm_length = float(input("Enter a length in centimeters: "))
        feet_length = cm_to_feet(cm_length)
        print(f"{cm_length} centimeters is equal to {feet_length:.2f} feet")
    else:
        print("Invalid choice. Please choose 1 or 2 for the conversion type.")

    another_conversion = input("Do you want to try another conversion? (yes/no): ")

    if another_conversion.lower() != "yes":
        print("Thank you for using the length conversion tool.")
        break
