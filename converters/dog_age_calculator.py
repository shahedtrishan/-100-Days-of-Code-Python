def dog_age_to_human_age(dog_age):
    if dog_age <= 2:
        human_age = dog_age * 10.5
    else:
        human_age = 21 + (dog_age - 2) * 4
    return human_age


while True:
    try:
        dog_age = float(input("Enter your dog's age in dog years: "))
        human_age = dog_age_to_human_age(dog_age)
        print(f"Your dog's age is approximately {human_age} human years.")

        another_calculation = input(
            "Do you want to calculate another dog's age? (yes/no): "
        )

        if another_calculation.lower() != "yes":
            print("Thank you for using the dog age calculator.")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number for your dog's age.")
