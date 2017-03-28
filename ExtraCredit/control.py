# Controller for Extra Credit
# Will contain all the methods for
# Adding items to the cart
# Removing items from the cart
# Calculating the subtotal
import tkinter as tk
import view
import model

class Controller:
    def __init__(self):
        root = tk.Tk()
        self.model = model.Model()
        self.view = view.MyFrame(self)
        self.view.mainloop()
    def createShopList(self):
        # Populates self.model.productList with items
        self.model.pamProducts()
        return self.model.productList

if __name__ == "__main__":
    c = Controller()