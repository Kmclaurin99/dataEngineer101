#
print (8/3)

#rounding decimals
print(round(8/3))

#rounding to certain number of decimals places
print(round(8/3, 3))
print(round(39/4, 6))

#use // f(x) to automatically convert to integers

results = 4/2
results /= 2
print(results)

score = 0
score += 2
print(score)

#f-strings; makes it easier to convert numerous different functions into a single function. compare line 22 vs. 23. Use curly brackets.
print("your score is " + str(score))
print(f"your score is {score}")

print(6 + 4 /2 - (1 * 2))