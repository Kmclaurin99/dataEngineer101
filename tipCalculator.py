#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator ")
bill_cost = float(input("How much was your bill? "))
tip_percent = int(input( "What percent would you like to tip? 10, 12, or 15? "))
bill_payers = int(input("How many people are splitting the bill? "))

cost_after_tip = round(bill_cost * ((tip_percent / 100) +1),2)

print(cost_after_tip)
bill_per_person = float(cost_after_tip / bill_payers)
print(round(bill_per_person,2))

