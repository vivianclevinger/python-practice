# Print statement to welcome user
print("Welcome to the tip calculator!")

# Variables storing user inputs as float and integer data types
bill = float(input("What was the total bill? $"))
tip = int(input("What tip percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

# Variables storing the results of mathematical operations used when calculating tip percentage, total tip , total bill, and split payment.
tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
split_payment = total_bill / 5

# Variable storing the split payment value formatted and rounded to 2 decimal places.
final_payment = ("%.2f" % round(split_payment, 2))

# Print statement utilizes f-string to concisely output string and float data types, without needing to convert types or concatenate.
print(f"Each person should pay: ${final_payment}")
