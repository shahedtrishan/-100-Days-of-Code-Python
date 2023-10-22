# Function to calculate the tip and total bill
def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip
    return tip, total_bill


while True:
    # Input the bill amount and tip percentage
    bill_amount = float(input("Enter the bill amount: $"))
    tip_percentage = float(input("Enter the desired tip percentage: "))

    # Calculate the tip and total bill
    tip, total_bill = calculate_tip(bill_amount, tip_percentage)

    # Display the results
    print(f"Bill Amount: ${bill_amount:.2f}")
    print(f"Tip ({tip_percentage}%): ${tip:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")

    another_calculation = input("Do you want to calculate another tip? (yes/no): ")

    if another_calculation.lower() != "yes":
        print("Thank you for using the tip calculator.")
        break
