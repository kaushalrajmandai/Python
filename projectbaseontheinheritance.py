# Parent class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

# Child class 1 - Manager
class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def show_manager_info(self):
        print("Role: Manager")
        print("Team Size:", self.team_size)

# Child class 2 - Developer
class Developer(Employee):
    def __init__(self, name, emp_id, programming_lang):
        super().__init__(name, emp_id)
        self.programming_lang = programming_lang

    def show_developer_info(self):
        print("Role: Developer")
        print("Programming Language:", self.programming_lang)




class Intern(Employee):
    def __init__(self, name, emp_id, duration):
        super().__init__(name, emp_id)
        # Assuming duration is in months based on the prompt
        self.duration = duration 

    def show_info(self):
        self.show_common_info()
        print("Role: Intern")
        print("Internship Duration (months):", self.duration)



print("Choose Employee Type:")
print("1. Manager")
print("2. Developer")
print("3. Intern")

# Get user input for choice
# Using try-except for robust input handling is good practice
try:
    choice = int(input("Enter your choice (1-3): "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Get common employee details
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

# Initialize employee variable
employee = None

if choice == 1:
    # Manager
    try:
        team_size = int(input("Enter team size: "))
        employee = Manager(name, emp_id, team_size)
    except ValueError:
        print("Invalid team size.")
        exit()

elif choice == 2:
    # Developer
    lang = input("Enter programming language: ")
    employee = Developer(name, emp_id, lang)

elif choice == 3:
    # Intern
    try:
        # Renamed variable from 'duration' to 'intern_duration' for clarity
        intern_duration = int(input("Enter internship duration (months): "))
        employee = Intern(name, emp_id, intern_duration)
    except ValueError:
        print("Invalid duration.")
        exit()

else:
    print("Invalid choice. Program terminated.")
    exit()

# Display the created employee's information
print("\n--- Employee Information ---")
if employee:
    employee.show_info()
