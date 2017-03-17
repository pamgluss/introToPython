# Homework 9: Shopping cart
# Pamela Gluss

# Shopping Cart class is for catching all the products you create
class ShoppingCart:
    def __init__(self):
        self.shoppingList = []
        self.subTotal = 0
    def addItem(self, item):
        self.shoppingList.append(item)
        item.shoppingQuantity += 1
    def getSubTotal(self):
        for item in self.shoppingList:
            self.subTotal += item.price
        return self.subTotal
    def subtractItem(self, item):
        if item in self.shoppingList:
            item.shoppingQuantity -= 1
            self.shoppingList.remove(item)
    def __str__(self):
        return "Your cart contains %s and %s. Your subtotal is %s" % (self.shoppingList[: -1], self.shoppingList[-1], self.subTotal)

# A generic product class that other, more specified products will be built on
class Product:
    def __init__(self, price, inventory, category):
        self.price = self.setPrice(price)
        self.shoppingQuantity = 0
        self.inventory = inventory
        self.productCategory = category

    def setPrice(self, price):
        return "$%i" % price

# Toy is a subclass of Product (Product > Toy)
class Toy(Product):
    def __init__(self, price, inventory, category, group):
        Product.__init__(self, price, inventory, category)
        self.ageGroup = self.setAgeGroup(group)
    def setAgeGroup(self, group):
        return group

#BabyToy is a subclass of both PRODUCT and TOY
# Product > Toy > Baby Toy
class BabyToy(Toy, Product):
    def __init__(self, price, inventory, category, group, name, safetyInfo):
        Product.__init__(self, price, inventory, category)
        Toy.__init__(self, price, inventory, category, group)
        self.name = name
        self.safetyInfo = safetyInfo
    def __str__(self):
        return "This baby toy costs %s and is called %s and use caution! %s" % (self.price, self.name, self.safetyInfo)

# Food is subclass of product
class Food(Product):
    def __init__(self, price, inventory, category):
        Product.__init__(self, price, inventory, category)
        self.expiration = ""
    def setExpirationDate(self, expiration):
        self.expiration = expiration

# Frozen Dessert is a subclass of Food and Product
# Product > Food > Frozen Dessert
class frozenDessert(Food, Product):
    def __init__(self, price, inventory, category, size, temperature):
        Food.__init__(self, price, inventory, category)
        Product.__init__(self, price, inventory, category)
        self.size = size
        self.refrigerationTemperature = temperature
    def __str__(self):
        return "This dessert costs %s and is a %s and needs to be at %s degrees" % (self.price, self.size, self.refrigerationTemperature)

sampleDessert = frozenDessert(5, 3, "Ice Cream", "Small", 27)
print(sampleDessert)

sampleBabyToy = BabyToy(15, 3, "Rattle", "Toddlers", "Baby R Us", "Do Not Put in Your Mouth")
print(sampleBabyToy)
