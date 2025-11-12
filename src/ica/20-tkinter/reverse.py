import tkinter as tk


# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.first_label = tk.Label(self.mainWin, text="first")
        self.first_label.grid(column=0, row=0)
        self.second_label = tk.Label(self.mainWin, text="second")
        self.second_label.grid(column=1, row=0)
        self.entry = tk.Entry(self.mainWin)
        self.entry.grid(column=2, row=0)
        self.entry.bind('<Return>', self.entry_response)
        self.entry.bind('<Tab>', self.entry_response)
    def run(self):
        self.mainWin.mainloop()

    def entry_response(self, event):
        text = self.entry.get()
        self.first_label["text"] = text[::-1]


# ----- Main program -----
myGui = BasicGui()
myGui.run()
