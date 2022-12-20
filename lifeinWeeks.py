# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#365 days in a year
#52 weeks in a year
#12 months in a year

#You have x days, y weeks, and z months left.

ninetyDays= (90 * 365)
ninetyWeeks= (90 * 52)
ninetyMonths= (90 * 12)

days= (ninetyDays) - (int(age) * 365) 
weeks= (ninetyWeeks) - (int(age) * 52) 
months= (ninetyMonths)- (int(age) * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left based on a life expectancy of 90 years old.")