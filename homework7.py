# Homework 7: Different types of employees
# Pamela Gluss

# Part 1: Define the Employee

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

# Tests methods for Employee
# cheryl = Employee("cheryl", "smith", 123456789, 40000)
# print(cheryl)
# cheryl.giveRaise(15)
# print(cheryl)

# Part 2: Define the Manager
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

# Part 3: Create a list of employee AND manager objects and loop to give everyone a raise
class EmployeeList:
    def __init__(self):
        self.list = []
    def addEmployee(self, employee):
        self.list.append(employee)
    def __str__(self):
        returnedString = ""
        for contact in self.list:
            returnedString = returnedString + "\n" + str(contact)
        return returnedString
    def giveRaiseAll(self):
        for contact in self.list:
            contact.giveRaise(15)

cheryl = Employee("Cheryl","Wilkerson",888559632,40000)
alyce = Employee("Alyce", "Von Damm", 777889245, 55000)
bob = Manager("Regional Manager", 900, "Bob", "Richards", 666776666, 75000)
erica = Manager("CTO", 50000, "Erica", "Langdon", 654882357, 825000)

testList = EmployeeList()
testList.addEmployee(cheryl)
testList.addEmployee(alyce)
testList.addEmployee(bob)
testList.addEmployee(erica)

print(testList)
testList.giveRaiseAll()
print(testList)