class EmployeeManagement:

    def __init__(self):
        self.employee = {}


    # ✅ Input validation
    def get_int(self, message):

        while True:
            try:
                return int(input(message))
            except ValueError:
                print("❌ Enter valid number")


    # 1. Add employee
    def add_employee(self, employee_ID, employee_Name, age, salary, department):

        if employee_ID in self.employee:

            print("❌ Employee ID already exists")
            return
        
        self.employee[employee_ID] = {

            "name": employee_Name,
            "age": age,
            "salary": salary,
            "department": department

        }

        print(f"✅ Employee {employee_Name} added successfully")

        self.save_to_file("data.txt")   # ⭐ ADDED HERE (Auto-save)



    # 2. View employee
    def view_employee(self):

        if self.employee:

            print(f"\n📊 Total Employees: {len(self.employee)}")

            for employee_ID, details in self.employee.items():

                print(f"""
Employee ID : {employee_ID}
Name        : {details['name']}
Age         : {details['age']}
Salary      : {details['salary']}
Department  : {details['department']}
""")
        else:
            print("❌ No employee added")



    # 3. Update employee
    def update_employee(self, employee_ID):

        if employee_ID not in self.employee:

            print("❌ Employee not found")
            return


        name = input("New Name (Enter skip): ")
        age = input("New Age (Enter skip): ")
        salary = input("New Salary (Enter skip): ")
        dept = input("New Department (Enter skip): ")


        if name:
            self.employee[employee_ID]["name"] = name

        if age:
            self.employee[employee_ID]["age"] = int(age)

        if salary:
            self.employee[employee_ID]["salary"] = int(salary)

        if dept:
            self.employee[employee_ID]["department"] = dept


        print("✅ Successfully updated")

        self.save_to_file("data.txt")   # ⭐ ADDED HERE (Auto-save)



    # 4. Remove employee
    def remove_employee(self, employee_ID):

        if employee_ID not in self.employee:

            print("❌ Employee not found")
            return
        
        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":

            emp = self.employee.pop(employee_ID)

            print(f"✅ Employee {emp['name']} removed successfully")

            self.save_to_file("data.txt")   # ⭐ ADDED HERE (Auto-save)

        else:
            print("❌ Delete cancelled")



    # 5. Save file
    def save_to_file(self, filename):

        try:

            with open(filename, 'w') as file:

                for employee_ID, details in self.employee.items():

                    line = f"{employee_ID}:->{details['name']},{details['age']},{details['salary']},{details['department']}\n"

                    file.write(line)


            # ⭐ ADDED HERE (Backup file)
            with open("backup.txt", "w") as backup:

                for employee_ID, details in self.employee.items():

                    line = f"{employee_ID}:->{details['name']},{details['age']},{details['salary']},{details['department']}\n"

                    backup.write(line)


            print("✅ Employee data saved successfully")

        except:
            print("❌ Error saving file")



    # 6. Load file
    def load_the_file(self, filename):

        try:

            with open(filename, 'r') as file:

                self.employee = {}

                for line in file:

                    id_part, details_part = line.strip().split(':->')

                    employee_ID = int(id_part)

                    name, age, salary, department = details_part.split(',')

                    self.employee[employee_ID] = {

                        "name": name,
                        "age": int(age),
                        "salary": int(salary),
                        "department": department

                    }

            print("✅ Employee data loaded successfully")

        except FileNotFoundError:

            print("❌ File not found")



    # 7. Search employee by ID
    def Search_Employee(self):

        employee_ID = self.get_int("Enter ID: ")

        if employee_ID in self.employee:

            print(self.employee[employee_ID])

        else:
            print("❌ Not found")



    # ⭐ ADDED HERE (Search by name)
    def search_by_name(self):

        name = input("Enter name: ")

        for emp_id, emp in self.employee.items():

            if emp["name"].lower() == name.lower():

                print(emp_id, emp)
                return

        print("❌ Not found")



    # 8. Salary report
    def Salary_Report(self):

        salaries = [emp['salary'] for emp in self.employee.values()]

        print("Highest:", max(salaries))
        print("Lowest:", min(salaries))
        print("Average:", sum(salaries)/len(salaries))



    # ⭐ ADDED HERE (Total salary)
    def total_salary(self):

        total = sum(emp["salary"] for emp in self.employee.values())

        print("Total salary:", total)



    # Login
    def login(self):

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "admin" and password == "1234":

            print("Login successful\n")
            return True

        else:
            print("Invalid login")
            return False



    # Main menu
    def main(self):

        while True:

            print("""
1 Add employee
2 View employee
3 Update employee
4 Delete employee
5 Save to file
6 Load file
7 Search employee by ID
8 Salary Report
9 Search by Name
10 Total Salary
11 Exit
""")

            choice = input("Enter choice: ")


            if choice == "1":

                emp_id = self.get_int("ID: ")
                name = input("Name: ")
                age = self.get_int("Age: ")
                salary = self.get_int("Salary: ")
                dept = input("Department: ")

                self.add_employee(emp_id, name, age, salary, dept)


            elif choice == "2":
                self.view_employee()

            elif choice == "3":
                emp_id = self.get_int("ID: ")
                self.update_employee(emp_id)

            elif choice == "4":
                emp_id = self.get_int("ID: ")
                self.remove_employee(emp_id)

            elif choice == "5":
                self.save_to_file("data.txt")

            elif choice == "6":
                self.load_the_file("data.txt")

            elif choice == "7":
                self.Search_Employee()

            elif choice == "8":
                self.Salary_Report()

            elif choice == "9":
                self.search_by_name()

            elif choice == "10":
                self.total_salary()

            elif choice == "11":

                confirm = input("Are you sure? yes/no: ")   # ⭐ ADDED HERE

                if confirm == "yes":

                    print("Exiting...")
                    break



# ⭐ ADDED HERE (Auto load at start)
obj = EmployeeManagement()

obj.load_the_file("data.txt")

if obj.login():

    obj.main()