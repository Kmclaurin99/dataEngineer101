# def greet():
#     print("Hello")
#     print("this is")
#     print("my greet function.")
# greet()

# Function that allows for input:
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
#     print("This is my greet function.")

# greet_with_name("Kwan")

# We basically just created a new varaible "name" and set it to "Kwan"
# "name" is our parameter and "Kwan" is our arguement

#Functions with more then one input
# def greet_with(name, location):
#     print(f"Hello, {name}")
#     print(f"Isnt the weather beautiful in {location}?")
# greet_with("Kwan", "Atlanta")
#This is called positional arguements

#Keyword arguements
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"Isnt the weather beautiful in {location}?")
greet_with(location = "Atlanta", name = "Kwan")