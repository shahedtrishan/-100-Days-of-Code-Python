import datetime

while True:
    # Input the date, month, and year
    day = int(input("Enter the day (1-31): "))
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year (e.g., 2023): "))

    # Create a datetime object with the provided date
    try:
        date = datetime.date(year, month, day)

        # Get the day of the week
        day_of_week = date.strftime("%A")

        # Print the result
        print(f"The day of the week for {day}/{month}/{year} is {day_of_week}.")
    except ValueError:
        print("Invalid date. Please check your input.")

    another_calculation = input("Do you want to calculate another date? (yes/no): ")

    if another_calculation.lower() != "yes":
        print("Thank you for using the date-to-day calculator.")
        break
