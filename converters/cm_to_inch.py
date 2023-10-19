def cm_to_inch(cm):
    inch = cm / 2.54
    return inch


def inch_to_cm(inch):
    cm = inch * 2.54
    return cm


while True:
    print("Choose the conversion type:")
    print("1. Centimeters to Inches")
    print("2. Inches to Centimeters")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        cm_length = float(input("Enter a length in centimeters: "))
        inch_length = cm_to_inch(cm_length)
        print(f"{cm_length} centimeters is equal to {inch_length:.2f} inches")
    elif choice == 2:
        inch_length = float(input("Enter a length in inches: "))
        cm_length = inch_to_cm(inch_length)
        print(f"{inch_length} inches is equal to {cm_length:.2f} centimeters")
    else:
        print("Invalid choice. Please choose 1 or 2 for the conversion type.")

    another_conversion = input("Do you want to try another conversion? (yes/no): ")

    if another_conversion.lower() != "yes":
        print("Thank you for using the conversion tool.")
        break
