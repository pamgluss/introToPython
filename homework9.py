# Homework 9: Shopping cart
# Pamela Gluss

# Shopping Cart class is for catching all the products you create
class ShoppingCart:
    def __init__(self):
        self.shoppingList = []
        self.subTotal = 0
    # addItem will append an object to the shopping list and increase the shopping quantity of that item if it doesn't already exist
    # in the list.
    def addItem(self, item):
        if item in self.shoppingList:
            item.shoppingQuantity += 1
        else:
            self.shoppingList.append(item)
            item.shoppingQuantity += 1

    # getSubTotal loops through the shopping list and adds up the price of each item
    # Adding it to the subtotal
    # I reset the subTotal every time I run this function.
    def getSubTotal(self):
        self.subTotal = 0
        for item in self.shoppingList:
            self.subTotal += item.price
        return self.subTotal

    # subtractItem is designed to take items out of the list.
    # First it checks if the item is in the list
    def subtractItem(self, item):
        if item in self.shoppingList:
            item.shoppingQuantity -= 1
            self.shoppingList.remove(item)
        else:
            return "This item is not in the cart."
    def __str__(self):
        itemNames = ""
        for item in self.shoppingList:
            itemNames += (item.name) + ", "
        return "Your cart contains {0}and {1}. Your subtotal is ${2}".format(itemNames, self.shoppingList[-1].name, self.getSubTotal())

# A generic product class that other, more specified products will be built on
class Product:
    def __init__(self, name, price, inventory, category):
        self.name = name
        self.price = price
        self.shoppingQuantity = 0
        self.inventory = inventory
        self.productCategory = category

    def setPrice(self, price):
        return "$%i" % price

# Toy is a subclass of Product (Product > Toy)
class Toy(Product):
    def __init__(self, name, price, inventory, category, group):
        Product.__init__(self, name, price, inventory, category)
        self.ageGroup = group
    def setAgeGroup(self, group):
        self.ageGroup = group

#BabyToy is a subclass of both PRODUCT and TOY
# Product > Toy > Baby Toy
class BabyToy(Toy, Product):
    def __init__(self, name, price, inventory, category, group, safetyInfo):
        Toy.__init__(self, name, price, inventory, category, group="Babies")
        self.safetyInfo = safetyInfo
    def __str__(self):
        return "This baby toy costs %s and is called %s and use caution! %s" % (self.price, self.name, self.safetyInfo)

# Food is subclass of product
class Food(Product):
    def __init__(self, name, price, inventory, category):
        Product.__init__(self, name, price, inventory, category)
        self.expiration = ""
    def setExpirationDate(self, expiration):
        self.expiration = expiration

# Frozen Dessert is a subclass of Food and Product
# Product > Food > Frozen Dessert
class FrozenDessert(Food, Product):
    def __init__(self, name, price, inventory, category, size, temperature):
        Food.__init__(self, name, price, inventory, category)
        self.size = size
        self.refrigerationTemperature = temperature
    def __str__(self):
        return "This dessert costs %s and is a %s and needs to be at %s degrees" % (self.price, self.size, self.refrigerationTemperature)

# These are testing whether the inheritance works. It does.
sampleDessert = FrozenDessert("SampleDessert", 6, 5, "Samples", "Medium", 21)
print(sampleDessert)

sampleBabyToy = BabyToy("SampleBabyToy", 15, 4, "Sample Toys", "Babies", "Danger")
print(sampleBabyToy)

# Now we're going to test the shopping cart
cheesecake = FrozenDessert("Cheesecake", 3, 3, "Cake", "Large", 27)
drumstick = FrozenDessert("Drumsticks", 8, 4, "Ice Cream", "Medium", 22)
rattle = BabyToy("Gumdrop Rattle", 2, 8, "Noise Maker", "Babies", "Contains Small Parts")
mobile = BabyToy("Stars and Galaxies Crib Mobile",18, 2, "Crib Accessory", "Babies", "Not for newborns.")

myShoppingCart = ShoppingCart()
myShoppingCart.addItem(cheesecake)
myShoppingCart.addItem(drumstick)
myShoppingCart.addItem(rattle)
myShoppingCart.addItem(mobile)

print(myShoppingCart)

