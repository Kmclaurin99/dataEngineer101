# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Leap Year= Year /4 = elif /100 elif / unless also divisbile by 400; Flowcharts help

if year % 4 == 0:
    print ("Leap year.")
elif year % 100 == 0:
    print ("Not leap year.")
elif year % 400 == 0:
    print ("Leap year.")
else:
    print ("Not leap year.")