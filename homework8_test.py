# Homework 8: Different types of employees
# Pamela Gluss
# Part 3: Create a list of employee AND manager objects

from employees_hw8 import Employee
from managers import Manager

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
    def sortList(self):
        self.list = sorted(self.list, key=lambda Employee: Employee.lastName)

cheryl = Employee("Cheryl", "Wilkerson",888559632,40000)
dan = Employee("Dan", "Abnett", 564224489, 45000)
alyce = Employee("Alyce", "Von Damm", 777889245, 55000)
bob = Manager("Regional Manager", 900, "Bob", "Richards", 666776666, 75000)
erica = Manager("CTO", 50000, "Erica", "Langdon", 654882357, 825000)
erica2 = Employee("Erica", "Langdon", 555224789, 60000)
erica3 = Employee("Erica", "Langdon", 645223174, 75000)
frank = Manager("VP",8000, "Frank", "Lebowitz", 666336457, 658400)
frank2 = Employee("Frank", "Von Damm", 258666234, 60000)

testList = EmployeeList()
testList.addEmployee(cheryl)
testList.addEmployee(dan)
testList.addEmployee(frank)
testList.addEmployee(frank2)
testList.addEmployee(alyce)
testList.addEmployee(bob)
testList.addEmployee(erica)
testList.addEmployee(erica2)

# Step 1: Compare two employees/managers to see if their first and last name are the same
print(erica == erica2)
print(erica2 == erica3)

print(erica == cheryl)
print(erica2 == cheryl)

# Step 2: Compare two employees/managers to see if the first comes before the second alphabetically
# Abnett comes before Wilkerson, Dan and Cheryl are both employees
print(dan < cheryl)
# Abnett comes before Richards, Dan is an employee, Bob is a manager
print(dan < bob)

# Alyce comes before Frank, and they have the same last name
print(alyce < frank2)

# Two guys named Frank, but Frank2's last name is Von Damm
print(frank2 < frank)

# Step 3: Sorting the full list
print(testList)
testList.sortList()
print(testList)

