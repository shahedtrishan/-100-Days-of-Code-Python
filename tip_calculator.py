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
