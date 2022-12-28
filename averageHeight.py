# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total = 0
for e in student_heights:
    total += e
 

number_of_students = 0
for f in student_heights:
    number_of_students +=1

Average = round(total / number_of_students)
print(Average)
