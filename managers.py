# Homework 8: Different types of employees
# Pamela Gluss
# Part 2: Define the Manager
from employees_hw8 import Employee
class Manager(Employee):
    def __init__(self, title, bonus, firstname, lastname, ssn, salary):
        Employee.__init__(self, firstname, lastname, ssn, salary)
        self.title = title
        self.bonus = bonus

    if __name__ == '__main__':
        def __str__(self):
            return super(Manager, self).__str__() + " %s %i" % (self.title, self.bonus)

    # Testing to make sure methods work
    # cherlene = Manager("VP of Accounting", 900, "Cherlene", "Kyler", 980558877, 90000)
    # print(cherlene)