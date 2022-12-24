# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#This code could have been much shorter by using string concactination.

lower_case1 = name1.lower()
lower_case2 = name2.lower()

t = lower_case1.count("t")
r = lower_case1.count("r")
u = lower_case1.count("u")
e = lower_case1.count("e")

t2 = lower_case2.count("t")
r2 = lower_case2.count("r")
u2 = lower_case2.count("u")
e2 = lower_case2.count("e")
sum = str((t+r+u+e+t2+r2+u2+e2))

l = lower_case1.count("l")
o = lower_case1.count("o")
v = lower_case1.count("v")
e = lower_case1.count("e")

l2 = lower_case2.count("l")
o2 = lower_case2.count("o")
v2 = lower_case2.count("v")
e2 = lower_case2.count("e")
sum2 = str((l+o+v+e+l2+o2+v2+e2))

sum3 = sum+sum2
sum4 = int(sum3)

if sum4 <10 or sum4 >90:
    print(f"Your score is {sum4}, you go together like coke and mentos.")
elif sum4 >=40 and sum4 <=50:
    print(f"Your score is {sum4}, you are alright together.")
else:
    print(f"Your score is {sum4}.")
