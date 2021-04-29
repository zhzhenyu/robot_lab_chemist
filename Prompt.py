import tkinter as tk
from tkinter import ttk


class Prompt(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text Box")
        self.window.minsize(300, 100)
        self.window.geometry("100x50+500+400")
        self.label = ttk.Label(self.window, text="Which Chemicals?")
        self.label.grid(column=1, row=0)
        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.window, width=15, textvariable=self.name)
        self.nameEntered.grid(column=1, row=1)
        self.button = ttk.Button(self.window, text="ok", command=self.clickme)
        self.button.grid(column=1, row=2)
        self.window.mainloop()

    def clickme(self):
        self.window.destroy()


class Merge(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text Box")
        self.window.minsize(300, 100)
        self.window.geometry("100x50+500+400")
        self.label = ttk.Label(self.window, text="What is the subtask?")
        self.label.grid(column=1, row=0)
        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.window, width=15, textvariable=self.name)
        self.nameEntered.grid(column=1, row=1)
        self.button = ttk.Button(self.window, text="ok", command=self.clickme)
        self.button.grid(column=1, row=2)
        self.window.mainloop()

    def clickme(self):
        self.window.destroy()


class Instruction(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text Box")
        self.window.minsize(300, 100)
        self.window.geometry("100x50+500+400")
        self.label = ttk.Label(self.window, text="What's the order of task?")
        self.label.grid(column=1, row=0)
        self.name = tk.StringVar()
        self.nameEntered = ttk.Entry(self.window, width=15, textvariable=self.name)
        self.nameEntered.grid(column=1, row=1)
        self.button = ttk.Button(self.window, text="ok", command=self.clickme)
        self.button.grid(column=1, row=2)
        self.window.mainloop()

    def clickme(self):
        self.window.destroy()
