def convert_weight(weight, from_unit, to_unit):
    units = {"kg": 1000, "g": 1, "mg": 0.001, "lb": 453.592, "oz": 28.3495}

    if from_unit in units and to_unit in units:
        converted_weight = weight * units[from_unit] / units[to_unit]
        return converted_weight
    else:
        return None


while True:
    from_unit = input("Enter the source unit (kg, g, mg, lb, oz): ")
    to_unit = input("Enter the target unit (kg, g, mg, lb, oz): ")
    weight = float(input(f"Enter the weight in {from_unit}: "))

    converted_weight = convert_weight(weight, from_unit, to_unit)

    if converted_weight is not None:
        print(f"{weight} {from_unit} is equal to {converted_weight:.2f} {to_unit}")
    else:
        print("Invalid units. Please check your input.")

    another_conversion = input("Do you want to perform another conversion? (yes/no): ")

    if another_conversion.lower() != "yes":
        print("Thank you for using the weight converter.")
        break
