from tkinter import *
from tkinter import Tk, ttk
root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
lbl = ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
btn = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)

print(dir(btn))
print(set(dir(btn)) - set(dir(frm)))

root.mainloop()