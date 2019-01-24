class Employee:
    raise_amount = 1.04
    num_of_employees = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_employees += 1

    def to_string(self):
        return self.first,self.last,self.email,self.pay

    def set_first(self, name):
        self.first = name

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

emp1 = Employee('John', 'Barrow', 50000)

print(emp1.to_string())
emp1.set_first("Mark")
emp1.apply_raise()
print(emp1.to_string())
print(Employee.num_of_employees)