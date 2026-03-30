students = [
    {"id": 101, "name": "Alice", "age": 20, "score": 85, "subject": ["Maths", "Gujarati", "English"]},
    {"id": 102, "name": "Bob", "age": 21, "score": 78, "subject": ["Maths", "Science", "English"]},
    {"id": 103, "name": "Charlie", "age": 19, "score": 92, "subject": ["Maths", "Hindi", "English"]}
]

while True:
    print("Welcome to the Student Data Organizer!")
    print("Select an Option: ")
    print("1. Add Student")
    print("2. Display all Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit!")
 
    
    choice=int(input("Select an option: "))
    match choice:
        case 1:
            id=int(input("Enter ID: "))
            name=input("Enter Name: ")
            age=int(input("Enter Age: "))
            score=int(input("Enter Score: "))
            subject=input("Enter Subjects (comma seperated): ").split(",")
            new_data={
                "id":id,
                "name":name,
                "age":age,
                "score": score,
                "subject": subject
            }
            students.append(new_data)
            print("Student added Successfully")
            print(students)
            #Add Student
        case 2:
            for student in students:
                print(f"ID: {student["id"]} | Name: {student["name"]} | Age: {student["age"] } | Score: {student["score"]} | Subject: {student["subject"]}")
                #Print Students
        case 3:
            for student in students:
                if student["id"]==102:
                    student["score"]=88
                    break
            print(students)
            #update Score
        case 4:
            for student in students:
                if student["id"] == 101:
                    students.remove(student)
                print(students)
                #delete student
        case 5:
            unique_subjects = set()
            for student in students:
                unique_subjects.update(student["subject"])
            print(unique_subjects)
            #unique subjects
        case 6:
            print("Exit!")
            break
