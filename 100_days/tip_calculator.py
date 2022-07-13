# Tip calculator to understand basics of python
# strings, variables, basic math, f-type strings

print("Welcome to the tip calculator!!")

bill_total = int(input("What is the total of the bill?"  + " "))
tip_percentage = int(input("What is the percentage tip would you like to give? 15, 20, or 25?" + " "))
bill_split = int(input("How many people will split the bill?" + " "))

amount_per_person = ((((tip_percentage / 100) * bill_total) + bill_total) / bill_split)
answer = (f"Each person should pay: ${round(amount_per_person, 2)}")
print(answer)
