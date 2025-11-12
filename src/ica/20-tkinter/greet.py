import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.quit_button = tk.Button(self.mainWin, text="Quit", command = self.quit_callback)
        self.quit_button.grid(column=0, row=0)
        self.hello_button = tk.Button(self.mainWin, text="Hello", command = self.change_hello)
        self.hello_button.grid(column=1, row=0)
        self.goodbye_button = tk.Button(self.mainWin, text="Goodbye", command = self.change_goodbye)
        self.goodbye_button.grid(column=2, row=0)
        self.label = tk.Label(self.mainWin, text="Welcome")
        self.label.grid(column=0, row=1)



    def run(self):
        self.mainWin.mainloop()

    def quit_callback(self):
        self.mainWin.destroy()

    def change_hello(self):
        self.label["text"] = "Hello"

    def change_goodbye(self):
        self.label["text"] = "Goodbye"



# ----- Main program -----
myGui = BasicGui()
myGui.run()
