# Contains the methods for the controller to use.
class Model:
    def __init__(self):
        self.productList = []
    def createStoreItem(self, name, price, stockQuantity):
        self.productList.append(Product(name, price, stockQuantity))
    def pamProducts(self):
        self.createStoreItem("Milk", 3.5, 5)
        self.createStoreItem("Eggs", 5.0, 7)
        self.createStoreItem("Bread", 2.35, 8)
        self.createStoreItem("Jam", 6.25, 3)
        self.createStoreItem("Chicken Breast", 9.0, 4)
        self.createStoreItem("Ice Cream", 4.60, 2)
    def calcSubTotal(self, list):
        subtotal = 0
        for sublist in list:
            subtotal += (sublist[3] * int(sublist[1].cget("text")))
        return subtotal
class Product:
    def __init__(self, name, price, stockQuantity):
        self.name = name
        self.price = price
        self.stockQuantity = stockQuantity


