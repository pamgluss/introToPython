# View for Extra Credit
# Sets up the frame and all the buttons / controls
import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller
        self.grid()

        # Create the label for "Store" in grid spot 0,0
        self.storeLabel = tk.Label()
        self.storeLabel["text"] = "Store"
        self.storeLabel.grid(row=0,column=0)

        # Create the label for "Cart" in grid spot 0,4
        self.cartLabel = tk.Label()
        self.cartLabel["text"] = "Cart"
        self.cartLabel.grid(row=0, column=4)
        self.cartRow = 1

        # This is a huge mess (but it works, somehow)
        # storeGrid is going to be the n x 4 grid (n being number of items, 4 being
        # 1. Item Name, 2. Item Price, 3. Item Quantity and 4. Add to Cart Button
        # createShopGrid is a method in view that contains the for loop for the shopping area
        # It takes in a list, which is found via controller's method of populating the store inventory.
        self.itemList = self.controller.createShopList()
        self.storeGrid = self.createShopGrid(self.itemList)

        # Create the button that will calculate the subtotal
        self.calcButton = tk.Button()
        self.calcButton["text"] = "Calculate Subtotal"
        self.calcButton.grid(row=len(self.itemList),column=5)

        # Create the label where the subtotal will appear
        self.subtotalLabel = tk.Label(text="0")
        self.subtotalLabel.grid(row=len(self.itemList),column=6)

    # View calls this method to create the shop grid (n x 4)
    def createShopGrid(self, list):
        self.shopRows = []
        for i in range(0, len(list)):
            self.newRow = []
            print("Testing", i)
            #Create the label for name
            self.newRow.append(tk.Label(text=list[i].name))
            self.newRow[0].grid(row=i+1, column=0)

            #Create the label for price
            self.newRow.append(tk.Label(text=list[i].price))
            self.newRow[1].grid(row=i+1, column=1)

            #Create the quantity spinner
            self.newRow.append(tk.Spinbox(format='%4.2f', from_=0, to=list[i].stockQuantity, wrap=True))
            self.newRow[2].grid(row=i+1, column=2)

            #Create "Add to Cart" Button
            #command = self.addToCart(list[i], self.shopRows[i][2].get())
            self.newRow.append(tk.Button(text="Add to Cart",
                                         command=lambda j = i: self.addToCart(list[j], 0)))
            self.newRow[3].grid(row=i+1, column=3)

            # Append the new row to the grid
            self.shopRows.append(self.newRow)

    def addToCart(self, object, quantity):
        print("add to cart test")
        self.cartItemLabel = tk.Label(text=object.name)
        self.cartItemLabel.grid(row=self.cartRow, column=4)

        self.cartQuantitylabel = tk.Label(text=quantity)
        self.cartItemLabel.grid(row=self.cartRow, column=4)

        self.rfcButton = tk.Button(text="Remove From Cart")
        self.rfcButton.grid(row=self.cartRow, column=4)

        self.cartRow +=1

