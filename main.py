#If the bill was $350.00, split between 5 people, with 15% tip. 
#Each person should pay (350.00 / 5) * 1.15 = 80.50
#Round the result to 2 decimal places.
print("Welcome to the best tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 15, 20, or 25? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")