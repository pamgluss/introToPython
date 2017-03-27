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
        self.view = view.MyFrame(self)
        self.model = model.Model()
        self.view.mainloop()

        # Populates self.model.productList with items
        self.model.pamProducts()
        self.storeInventory = self.model.productList
        self.view.createShopGrid(self.storeInventory)

if __name__ == "__main__":
    c = Controller()