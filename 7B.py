class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name, self.emp_id, self.department, self.salary = name, emp_id, department, salary

    def display_details(self):
        print("Employee Details")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)
        print("Salary:", self.salary)

    def update_salary(self, new_salary):
        self.salary = new_salary
        print("Updated Salary:", self.salary)

employees = [Employee(input("Enter Employee name: "), input("Enter Employee ID: "),
                     input("Enter Employee Department: "), int(input("Enter Employee Salary: ")))
             for _ in range(int(input("Enter the Number of Employees: ")))]

department = input("Enter the department to update salaries: ")
new_salary = int(input("Enter the new salary: "))

for employee in employees:
    if employee.department == department:
        employee.update_salary(new_salary)
