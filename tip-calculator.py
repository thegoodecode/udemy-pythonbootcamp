#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

bill = int(input("What was the total bill? €"))
tip = int(input("How much would you like to tip? 10, 15 or 20%
?"))

split = int(input("How many people want to split the bill? "))

bill_with_tip = int(tip / 100 * bill + bill)

bill_per_person = round((bill_with_tip / split), 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: €{final_amount}")