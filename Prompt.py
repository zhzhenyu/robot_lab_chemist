import tkinter as tk
from tkinter import ttk


class Prompt(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text Box")
        self.window.minsize(300, 100)
        self.label = ttk.Label(self.window, text="What is this task?")
        self.label.grid(column=0, row=0)
        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.window, width=15, textvariable=self.name)
        self.nameEntered.grid(column=0, row=1)
        self.button = ttk.Button(self.window, text="ok", command=self.clickme)
        self.button.grid(column=0, row=2)
        self.window.mainloop()

    def clickme(self):
        self.window.destroy()
