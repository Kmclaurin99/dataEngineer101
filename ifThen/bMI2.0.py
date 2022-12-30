# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#"Your BMI is 22, you have a normal weight."
#"Your BMI is 28, you are slightly overweight."
#"Your BMI is 33, you are obese."
#"Your BMI is 40, you are clinically obese."

#Write your code below this line 👇

MassIndex = round(weight / (height ** 2))

Index = int(MassIndex)

BMI = (f"Your BMI is {Index}")

if Index <= 18:
    print ("f{BMI}, you are underweight.")
elif Index <= 25:
    print (f"{BMI}, you have a normal weight.")
elif Index <= 30:
    print (f"{BMI}, you are slightly overweight.")
elif Index <= 35:
    print (f"{BMI}, you are obese.")
else:
    print (f"{BMI}, you are clinically obese.")


