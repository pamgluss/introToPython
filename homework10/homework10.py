# Pamela Gluss
# Homework 10

import tkinter as tk

class MyFrame(tk.Frame):
    # MyFrame will contain a user input, two buttons for F and C, and a quit button
    ## View ##
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack({"side":"left"})

        # Create the number entry field
        self.numEntry = tk.Entry()
        self.numEntry.insert(0, 0)
        self.numEntry.pack({"side":"left"})

        # Create Output
        self.outputLabel = tk.Label()
        self.outputLabel["text"] = "0"
        self.outputLabel.pack({"side":"left"})

        # Create the button for Farenheit (Temp will be F by default)
        self.convertF = tk.Button()
        self.convertF["text"] = "Convert to F"
        self.convertF["command"] = self.convertToF
        self.convertF.pack({"side":"left"})

        # Create the button for Celsius
        self.convertC = tk.Button()
        self.convertC["text"] = "Convert to C"
        self.convertC["command"] = self.convertToC
        self.convertC.pack({"side":"left"})

        # Create a quit button
        self.quitButton = tk.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        self.quitButton.pack({"side":"right"})

    ## Control ##
    def convertToF(self):
        tempIn = self.numEntry.get()

        try:
            tempOut = ((5 / 9) * (int(tempIn) - 32))
            self.outputLabel["text"] = str(tempOut) + "F"
        except ValueError:
            self.outputLabel["text"] = "Invalid Number"
            return "Invalid Number"
    def convertToC(self):
        tempIn = self.numEntry.get()
        try:
            tempOut = ((9 / 5) * int(tempIn)) + 32
            self.outputLabel["text"] = str(tempOut) + "C"
        except ValueError:
            self.outputLabel["text"] = "Invalid Number"
            return "Invalid Number"
    ## Model ##
if __name__ == "__main__":
    root = tk.Tk()
    view = MyFrame()
    view.mainloop()