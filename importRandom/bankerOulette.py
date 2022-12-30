# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number1 = len(names)
number = random.randint(0, number1 -1)

payer = names[number]

print(f"{payer} is going to buy the meal today!")

#We can use random.choice(names) to make this much easier



