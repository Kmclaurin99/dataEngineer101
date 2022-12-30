#"random" is a module created by the python team to allow for us to easily create random numbers.
#I can use the import function to import previously written code from previous .py files
#The random.randint function is good for random whole numbers

# import random

# random_integer = random.randint(0, 5)
# print(random_integer)

# #The random.random function is good for random float numbers between [0.0, 1.0)

# random_float = random.random()
# print(random_float)

# #What if I wanted a random float between [0, 5)?

# ran_dec = (random_float * 5)
# print(ran_dec)

# # Using the random.randint function to create a shortcut for my love calculator game. 

# love_score = random.randint(0,100)
# print(f"Your love score is {love_score}.")

# #Lists
# states_of_america = ["flordia", "georgia", "new york", "chicago", "texas", "alabama"]

# #The item in the lists will get numbered in relation to its placement in the brackets (remember to start at 0)
# print(states_of_america[4])

# #We can also count backwards if its easier
# print(states_of_america[-3])

# #Items inside the list can be altered easily
# states_of_america[2] = "New York"
# print(states_of_america[2])

# #.append function can be used to add a single item to the end of the lists
# states_of_america.append("New Mexico")
# print(states_of_america)

# #.extend function to add lists to an already lists
# states_of_america.extend["Wyoming", "San Diego"]
# print(states_of_america)

#We can combine two lists by using something called a 'nested lists'
fruits = ["apples", "oranges", "bananas"]
vegetables = ["kale", "spinach", "cabbage"]
healthy_foods = [fruits, vegetables] 
print(healthy_foods[1][1])
