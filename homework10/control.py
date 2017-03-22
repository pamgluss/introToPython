import tkinter as tk
import view
import model

class Controller:
    def __init__(self):
        self.view = view.MyFrame(self)
        self.model = model.Model()
        self.view.mainloop()

    # method that converts the number to Farenheit
    def convertToF(self):
        self.model.temperature_ = int(self.view.entryField.get())
        self.view.entryField.insert(tk.END, "C")
        self.view.outputLabel["text"] = str(self.model.convertToFar()) + "F"
        # tempIn = self.view.entryField.get()
        # try:
        #     tempOut = ((5 / 9) * (int(tempIn) - 32))
        #     self.view.outputLabel["text"] = str(tempOut) + "F"
        # except ValueError:
        #     self.view.outputLabel["text"] = "Invalid Number"
        #     return "Invalid Number"

    def convertToC(self):
        self.model.temperature_ = int(self.view.entryField.get())
        self.view.entryField.insert(tk.END, "F")
        self.view.outputLabel["text"] = str(self.model.convertToCel()) + "C"
        # tempIn = self.view.entryField.get()
        # try:
        #     tempOut = ((9 / 5) * int(tempIn)) + 32
        #     self.view.outputLabel["text"] = str(tempOut) + "C"
        # except ValueError:
        #     self.view.outputLabel["text"] = "Invalid Number"
        #     return "Invalid Number"

if __name__ == "__main__":
    c = Controller()