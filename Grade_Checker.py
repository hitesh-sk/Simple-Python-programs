# This is a program which gets an input from user and outputs the grade

num = int(input("Enter your marks \n"))

if num >= 90:
  grade = "A"
elif num >= 80 and num < 90:
  grade = "B"
elif num >= 70 and num < 80:
  grade = "C"
elif num >= 60 and num < 70:
  grade = "D"
else:
  grade = "F"

print("Your grade is:" grade)
