# View for Extra Credit
# Sets up the frame and all the buttons / controls
import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller
        self.cartRowCounter = 1
        self.grid()

        # Create the label for "Store" in grid spot 0,0
        self.storeLabel = tk.Label()
        self.storeLabel["text"] = "Store"
        self.storeLabel.grid(row=0,column=0)

        # Create the label for "Cart" in grid spot 0,4
        self.cartLabel = tk.Label()
        self.cartLabel["text"] = "Cart"
        self.cartLabel.grid(row=0, column=4)
    # Control calls this method to create the shop grid (n x 4)
    def createShopGrid(self, list):
        for i in range(1, len(list)):
            #Create the label for name
            self.nameLabel = tk.Label(text=list[i].name)
            self.nameLabel.grid(row=i, column=0)

            #Create the label for price
            self.priceLabel = tk.Label()
            self.priceLabel["text"] = list[i].price
            self.priceLabel.grid(row=i, column=1)

            #Create the quantity spinner
            self.spinnerBox = tk.Spinbox(format='%4.2f', from_=0, to=list[i].stockQuantity, wrap=True)
            self.spinnerBox.grid(row=i, column=2)

            #Create "Add to Cart" Button
            self.addToCartButton = tk.Button(default=tk.DISABLED)
            self.addToCartButton["text"] = "Add to Cart"
            self.addToCartButton["command"] = self.addToCart(list[i])
            self.addToCartButton.grid(row=i, column=3)

    def addToCart(self, object):
        pass