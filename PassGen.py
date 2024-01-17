from tkinter import *
from tkinter.ttk import *
import random
import pyperclip
from tkinter.messagebox import showinfo

def generate_password():
    length = length_var.get()
    chars = {
        1: "abcdefghijklmnopqrstuvwxyz",
        0: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        3: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    }
    password = ''.join(random.choice(chars[value_var.get()]) for _ in range(length))
    entry.delete(0, END)
    entry.insert(10, password)

def copy_password():
    pyperclip.copy(entry.get())

def about():
    showinfo("Help", "Made by Harshit & Sumit")

root = Tk()
root.geometry("550x80")
root.resizable(0, 0)
root.title("Password generator")

value_var = IntVar()
length_var = IntVar(value=7)

MenuBar = Menu(root)
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="Help", command=about)
MenuBar.add_cascade(label="About", menu=HelpMenu)
root.config(menu=MenuBar)

Label(root, text="Password").grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

Label(root, text="Length").grid(row=1)
Button(root, text="Copy", command=copy_password).grid(row=0, column=2)
Button(root, text="Generate", command=generate_password).grid(row=0, column=3)

for i, (text, val) in enumerate([("Easy", 1), ("Medium", 0), ("Hard", 3)], start=2):
    Radiobutton(root, text=text, variable=value_var, value=val).grid(row=1, column=i, sticky="E")

combo = Combobox(root, textvar=length_var, values=tuple(range(7, 25)))
combo.current(0)
combo.grid(row=1, column=1)

root.mainloop()
