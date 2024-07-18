# Tip-Calculator
100 Days of Code: Day 2 - Tip Calculator

# Tip Calculator

A simple Python program that calculates how much each person should pay when a bill is split among multiple people, including a tip percentage.

## How It Works

1. The program starts by welcoming the user.
2. It asks the user for three pieces of information:
   - The total bill amount.
   - The desired tip percentage (15%, 20%, or 25%).
   - The number of people splitting the bill.
3. It calculates the total tip amount and the total bill amount.
4. It calculates how much each person should pay by dividing the total bill by the number of people.
5. Finally, it rounds the result to two decimal places and displays the amount each person should pay.

## Example

Let's say the user inputs the following:
- Total bill amount: $350.00
- Tip percentage: 15%
- Number of people: 5

The program will output:
Each person should pay: $80.50


## The Code

Here is the Python code for the Tip Calculator:

```python
# Welcome message
print("Welcome to the best tip calculator!")

# Get user inputs
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 15, 20, or 25? "))
people = int(input("How many people to split the bill?"))

# Calculate the tip and total amounts
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# Display the result
print(f"Each person should pay: ${final_amount}")

