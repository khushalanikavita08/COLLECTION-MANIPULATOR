print("Welcome to the Student Data Organizer!")

students = []

while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter student details:")
        student_id = input("Student ID: ")
        full_name = input("Name: ")
        age =int(input("Age: "))
        grade_level = input("Grade: ")
        birth_date = input("Date of Birth (YYYY-MM-DD): ")
        subjects_input = input("Subjects : ")

        new_student = {
            "id": student_id,
            "name": full_name,
            "age": age,
            "grade": grade_level,
            "dob": birth_date,
            "subjects": subjects_input
        }

        students.append(new_student)
        print("\n")
        print("Student added successfully!")
    elif choice == "2":
        print("\n===== Student Records =====")
        if not students:
            print("No students found.")
        else:
            for student in students:
                print("ID:", student["id"],
                      " Name:", student["name"],
                      "Age:", student["age"],
                      "Grade:", student["grade"], 
                      "DOB:", student["dob"],
                      "Subjects:", student["subjects"])

    elif choice == "3":
        updated_id = input("Enter Student ID to update: ")
        found = False

        for s in students:
            if s["id"] == updated_id:
                print("Enter new details")
                s["name"] = input("Enter new name: ")
                s["age"] = input("Enter new age: ")
                s["grade"] = input("Enter new grade: ")
                s["dob"] = input("Enter new birth date (YYYY-MM-DD): ")
                s["subjects"] = input("Enter new subjects: ")

                print("Student updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")    
    elif choice == "4":
        delete_id = input("Enter Student ID to delete: ")
        found = False

        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                
                break

        if not found:
            print("Student not found.")     
    elif choice == "5":
        print("\n===== Subjects Offered =====")

        if not students:
            print("No students found.")
        else:
            subjects = set()

            for student in students:
                subjects.add(student["subjects"])

            print("Subjects Offered:")
            for sub in subjects:
                print(sub)   
    elif choice == "6":
        print("Thank you for using the Student Data Organizer!")
        break



 

