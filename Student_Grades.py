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
