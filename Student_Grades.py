def add_student(student_grades):
  """Adds a new student and their grade to the dictionary."""
  name = input("Enter student name: ")
  grade = input("Enter student grade: ")
  student_grades[name] = grade
  print(f"Added {name} with grade {grade}")

def update_student(student_grades):
  """Updates an existing student's grade in the dictionary."""
  name = input("Enter the name of the student to update: ")
  if name in student_grades:
    new_grade = input(f"Enter the new grade for {name}: ")
    student_grades[name] = new_grade
    print(f"Updated {name}'s grade to {new_grade}")
  else:
    print(f"Student {name} not found.")

def print_grades(student_grades):
  """Prints all student names and their grades."""
  if not student_grades:
    print("No student grades available.")
  else:
    print("Student Grades:")
    for name, grade in student_grades.items():
      print(f"{name}: {grade}")

print("Welcome to the Student Grade Management Program!")

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Update Student Grade")
    print("3. Print All Grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student(student_grades)
    elif choice == '2':
        update_student(student_grades)
    elif choice == '3':
        print_grades(student_grades)
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
