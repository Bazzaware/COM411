class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for employee in self.employee_list:
            print(f"{employee.full_name } £{employee.get_salary()}")
