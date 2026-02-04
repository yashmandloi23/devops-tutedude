# Student Grades Management Program

students = {}

while True:
    print("Student Grade Manager")
    print("1. Add new student")
    print("2. Update student grade")
    print("3. Print all grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")

        if name in students:
            print("Student already exists.")
        else:
            students[name] = grade
            print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        if len(students) == 0:
            print("No records found.")
        else:
            print("Student Grades: ")
            for name, grade in students.items():
                print(name, ":", grade)

    elif choice == "4":
        print("End")
        break

    else:
        print("Invalid choice.")
