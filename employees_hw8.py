# Homework 8: Different types of employees
# Pamela Gluss
# Part 1: Define the Employee
from functools import total_ordering
@total_ordering
class Employee(object):
    def __init__(self, firstname, lastname, ssn, salary):
        self.firstName = firstname
        self.lastName = lastname
        self.SSN = ssn
        self.salary = salary

    def __str__(self):
        return "%s %s %i %i" % (self.firstName, self.lastName, self.SSN, self.salary)

    def giveRaise(self, percentRaise):
        self.salary *= (1 + percentRaise/100)

    def __eq__(self, other):
        if (self.firstName).lower() is (other.firstName).lower() and (self.lastName).lower() is (other.lastName).lower():
            return True
        else:
            return False
    def __lt__(self, other):
        if self.lastName.lower() < other.lastName.lower():
            return True
        elif self.lastName.lower() is other.lastName.lower():
            if self.firstName.lower() < other.firstName.lower():
                return True
            else:
                return False
        else:
            return False

# Tests methods for Employee
# cheryl = Employee("cheryl", "smith", 123456789, 40000)
# print(cheryl)
# cheryl.giveRaise(15)
# print(cheryl)