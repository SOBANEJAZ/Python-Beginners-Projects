import tkinter as tk

class calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry = "337x667"
        self.window.resizable(0,0)
        self.window.title("Calculator")
    
    def run(self):
        self.window.mainloop()
        