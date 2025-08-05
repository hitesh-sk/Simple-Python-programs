# Simple-Python-programs
Simple-Python-programs
1. Grade Checker
# Take a score as input and print the grade based on the provided input:
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

print("Your grade is:", grade)


2. Student Grades

# Initialize an empty dictionary
grades = {}

while True:
    print("\nChoose an option:")
    print("1. Add new student")
    print("2. Update existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in grades:
            print(f"{name} already exists with grade {grades[name]}")
        else:
            grade = input("Enter grade: ")
            grades[name] = grade
            print(f"Student {name} added with grade {grade}")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in grades:
            grade = input("Enter new grade: ")
            grades[name] = grade
            print(f"{name}'s grade updated to {grade}")
        else:
            print(f"Student {name} not found.")

    elif choice == "3":
        if not grades:
            print("No student data available.")
        else:
            print("\nStudent Grades:")
            for name, grade in grades.items():
                print(f"{name}: {grade}")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")

3. Write to a File

# a program to create a text file and write some content to it

# Open a file in write mode ('w' will create the file if it doesn't exist)
file = open("example.txt", "w")

# Write some content to the file
file.write("Hello, this is a sample text file.\n")
file.write("This line is written using Python.\n")
file.write("File operations are easy!\n")

# Close the file to save changes
file.close()

print("File created and content written successfully.")

4. Read from a File

# Open the file in read mode
file = open("example.txt", "r")

# Read the entire content of the file
content = file.read()

# Print the content
print("File content:")
print(content)

# Close the file
file.close()
