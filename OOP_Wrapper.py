print("""--- "Python OOP Project: Employee Management System---"
Choose an Operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Check Subclass
6. Exit"""
)

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
                
    def display(self):
        print(f"Person created with name: {self.name} and age:{self.age}.")
            
class Employee(Person):
    def __init__(self, employee_id=None, name=None, age=None, salary=None):
        super().__init__(name,age)
        self.__employee_id=employee_id
        self.__salary=salary
    def get_employee_id(self):
        return self.__employee_id
        
    def set_employee_id(self, emp_id):
        self.__employee_id=emp_id
        
    def get_salary(self):
        return self.__salary
        
    def set_salary(self, salary):
        self.__salary=salary
        
    def set_data(self, employee_id=None, name=None, age=None, salary=None):
        if employee_id and name and age and salary:
            self.__employee_id=employee_id
            self.name=name
            self.age=age
            self.__salary=salary
        elif name and age:
            self.name=name
            self.age=age
        else:
            print("Insufficient Data")
            
    def display(self):
        super().display()
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: {self.__salary}")
        
    def __del__(self):
        print("Employee object deleted")
        
class Manager(Employee):
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department=department
        
    def display(self):
        super().display()
        print(f"Department: {self.department}")
        
class Developer(Employee):
    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language=programming_language
        
    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")
        

while True:
    choice = int(input("\nEnter your Choice:"))
    
    match choice:
        case 1:
            p=Person("Alice", 30)
            print("\nPerson Created:")
            p.display()
            
        case 2:
            e=Employee()
            e.set_data("E123", "John Grande", 45, 50000.0)
            print("\nEmployee Created:")
            e.display()
            
        case 3:
            m=Manager("M101", "Sharon", 40, 80000.0, "HR")
            print("\nManager Created")
            m.display()
        
        case 4:
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            
            sub_choice=int(input("Enter your choice: "))
            
            if sub_choice==1:
                p=Person("Alice", 30)
                print("\nPerson Details:")
                p.display()
                
            elif sub_choice==2:
                e=Employee("E123", "John Grande", 45, 50000.0)
                print("\nEmployee Details:")
                e.display()
                
            elif sub_choice==3:
                m=Manager("M101", "Sharon", 40, 80000.0, "HR")
                print("\nManager Details:")
                m.display()
                
        case 5:
            print("\nIs Manager subclass of Employee?", issubclass(Manager, Employee))
            print("\nIs Developer subclass of Employee?", issubclass(Developer, Employee))
                
        case 6:
            print("Exiting")
            break
        
        case _:
            print("Invalid Choice")
            break