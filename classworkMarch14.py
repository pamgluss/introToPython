import tkinter

class MyFrame(tkinter.Frame):
    """
    class MyFrame is a tkinter.Frame that contains two Buttons and a Label. One Button increments a counter and the other Button quits. The Label is used to give the user information.
    """
    def __init__(self):
        """
        Places the controls onto the Frame.
        """
        tkinter.Frame.__init__(self)   # initializes the superclass
        self.pack()   #  required in order for the Buttons to show up properly
        self.counter = 0

        #set up the increment Button
        self.incrementButton = tkinter.Button(self)
        self.incrementButton["text"] = "Increment"
        self.incrementButton.pack({"side": "left"})

        #set up the Label
        self.labelForOutput = tkinter.Label(self)
        self.labelForOutput["text"] = 0
        self.incrementButton["command"] = self.addOne
        self.labelForOutput.pack({"side": "left"})

        # Set up entry for name
        self.nameEntry = tkinter.Entry()
        self.nameEntry.insert(0, "your name here")
        self.nameEntry.pack({"side": "left"})

        # set up button for Say Hi method
        self.hiButton = tkinter.Button(self)
        self.hiButton["text"] = "Hello",
        self.hiButton["command"] = self.sayHi
        self.hiButton.pack({"side": "left"})

        self.greeting = tkinter.Label(self)
        self.greeting.pack({"side": "left"})

        #set up the quit Button
        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        self.quitButton.pack({"side": "left"})

    def addOne(self):
        self.counter = self.counter + 1
        self.labelForOutput["text"] = self.counter

    def sayHi(self):
        """ greets the user by taking text from the nameEntry widget
            and putting it into the greeting widget
        """
        self.greeting["text"] = "Hello " + self.nameEntry.get()

if __name__ == "__main__":
    root = tkinter.Tk()
    view = MyFrame()  # puts the Frame onto the user's screen
    view.mainloop()