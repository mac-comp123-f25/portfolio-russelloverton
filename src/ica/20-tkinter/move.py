import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.easel = tk.Canvas(background="pink")
        self.easel.grid(column=0, row=0)
        text_id = self.easel.create_text(100, 100, text="Russell", fill="blue")
    def run(self):
        self.mainWin.mainloop()

    def move_callback(self, event):


# ----- Main program -----
myGui = BasicGui()
myGui.run()