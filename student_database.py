class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print("Error: Student is already enrolled.")
        else:
            self.__is_enrolled = True
            print("Student enrolled successfully.")

    def drop_student(self):
        if not self.__is_enrolled:
            print("Error: Student is not enrolled.")
        else:
            self.__is_enrolled = False
            print("Student dropped successfully.")

    def view_student_info(self):
        print("\n--- Student Info ---")
        print("ID:", self.__student_id)
        print("Name:", self.__name)
        print("Department:", self.__department)
        print("Enrolled:", self.__is_enrolled)


def find_student(sid):
    for student in StudentDatabase.student_list:
        if student._Student__student_id == sid:
            return student
    return None


while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Enroll Student")
    print("4. Drop Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        status = input("Is Enrolled? (yes/no): ")

        is_enrolled = True if status.lower() == "yes" else False

        Student(sid, name, dept, is_enrolled)
        print("Student added successfully!")

    elif choice == "2":
        if len(StudentDatabase.student_list) == 0:
            print("No students found!")
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()

    elif choice == "3":
        sid = int(input("Enter Student ID to enroll: "))
        student = find_student(sid)

        if student is None:
            print("Error: Invalid Student ID.")
        else:
            student.enroll_student()

    elif choice == "4":
        sid = int(input("Enter Student ID to drop: "))
        student = find_student(sid)

        if student is None:
            print("Error: Invalid Student ID.")
        else:
            student.drop_student()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")