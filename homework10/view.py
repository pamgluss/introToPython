import tkinter as tk
import control

class MyFrame(tk.Frame):
    # MyFrame will contain a user input, two buttons for F and C, and a quit button
    ## View ##
    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller
        self.pack({"side":"left"})

        # Create Input
        self.entryField = tk.Entry()
        self.entryField.insert(0, 0)
        self.entryField.pack({"side": "left"})
        self.tempIn = 0

        # Create Output
        self.outputLabel = tk.Label()
        self.outputLabel["text"] = "0"
        self.outputLabel.pack({"side": "left"})

        # Create the button for Fahrenheit (Temp will be F by default)
        self.convertF = tk.Button()
        self.convertF["text"] = "Convert to F"
        self.convertF["command"] = self.convertToF
        self.convertF.pack({"side": "left"})

        # Create the button for Celsius
        self.convertC = tk.Button()
        self.convertC["text"] = "Convert to C"
        self.convertC["command"] = self.convertToC
        self.convertC.pack({"side": "left"})

        # Create a quit button
        self.quitButton = tk.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        self.quitButton.pack({"side": "right"})

    def convertToF(self):
        return self.controller.convertToF()
    def convertToC(self):
        return self.controller.convertToC()