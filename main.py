# Greetings to my first project called as tip calculator
print("Welcome to the tip calculator!")

# First enter the total amount of bill
bill = float(input("Enter the amount of bill: $"))

# Then enter what percentage of tip will be given
tip = int(input("Enter the percentage of bill (10, 12, or 15) : %"))

# Then enter amoung how many people the total bill will be devided
people = int(input("Enter the number of people: "))

# Let's start the calculation of tip with bill
tip_percentage = tip / 100
bill_with_tip = tip_percentage * bill
total_bill = bill_with_tip + bill

# Then devide total bill among people
per_person = total_bill / people

# After that we need to round the final amount into 2 decimal units
total_amount = round(per_person, 2)
total_amount = "{:.2f}".format(total_amount)

# Finally, by using F-strings print how much should be paid per person
print(f'Each person should pay {total_amount} dollars')
