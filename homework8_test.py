# Homework 8: Different types of employees
# Pamela Gluss
# Part 3: Create a list of employee AND manager objects

from employees import Employee
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


cheryl = Employee("Cheryl","Wilkerson",888559632,40000)
dan = Employee("Dan", "Abnett",564224489, 45000)
alyce = Employee("Alyce", "Von Damm", 777889245, 55000)
bob = Manager("Regional Manager", 900, "Bob", "Richards", 666776666, 75000)
erica = Manager("CTO", 50000, "Erica", "Langdon", 654882357, 825000)
frank = Manager("VP",8000, "Frank", "Lebowitz", 666336457, 658400)

testList = EmployeeList()
testList.addEmployee(cheryl)
testList.addEmployee(dan)
testList.addEmployee(frank)
testList.addEmployee(alyce)
testList.addEmployee(bob)
testList.addEmployee(erica)

# Check current list
print(testList)
testList.sortList()
print(testList)