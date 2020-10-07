import tkinter
from tkinter import Tk, Button, Label, Entry, DoubleVar

window = Tk()
window.title("feet to meter conversion")
window.configure(background = "lightgreen")
window.geometry("400x300")
window.resizable(width = True, height = True)

def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set("%.4f" % meter)

def clear():
    ft_value.set("")
    mt_value.set("")

ft_lbl = Label(window, text="Feet", bg="purple", fg="white", width=14)
ft_lbl.grid(row=0, column=0, padx=30, pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable = ft_value, width = 14)
ft_entry.grid(column = 1, row = 0)
ft_entry.delete(0, 'end')

mt_lbl = Label(window, text="Meter", bg="red", fg="white", width=14)
mt_lbl.grid(row=1, column=0)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(row=1, column=1, pady=30)
mt_entry.delete(0, 'end')

convert_btn = Button(window, text="convert", bg="green", fg="white", width=14, command=convert)
convert_btn.grid(row=3, column=0, padx=30)

clear_btn = Button(window, text="clear", bg="black", fg="white", width=14, command=clear)
clear_btn.grid(row=3, column=1, padx=30)

window.mainloop()
