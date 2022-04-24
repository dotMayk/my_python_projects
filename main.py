def bill_calculator(total, tip, people):
    amount = (total + (total * (tip / 100))) / people
    return amount


print("Welcome to the TIP CALCULATOR!")

bill_total = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? "))
people_to_split = int(input("How many people are going to split the bill? "))

amount_per_person = bill_calculator(bill_total, tip_percentage, people_to_split)
print(f"Each person should pay: {amount_per_person:.2f}")
