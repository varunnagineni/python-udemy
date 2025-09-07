print("elcome to the tip calculator!")
total_bill = input("What was the total bill?")
print(total_bill)
tip_percent = int(input("How much tip would you like to give? 10, 12, 15, 20?"))
tip_percent /= 100
print(f"tip percent is : {tip_percent}")

bill_with_tip = float(total_bill) * (1+tip_percent)
print(bill_with_tip)

split = int(input("How many people to split the bill?"))

final_amount_per_person = bill_with_tip / split
print(final_amount_per_person)

final_amount = round(final_amount_per_person, 2)
print(f"Each person should pay : ${final_amount}")