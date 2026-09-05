from fractions import Fraction
import tkinter as tk

def check(a):
    x1 = a[0]
    x2 = a[1]
    if x1.count("-") > 1: return False
    if x1.count("-") == 1 and x1[0] != "-": return False
    if x1 == "" or x2 == "" or x2 == "0": return False
    for i in x1:
        if i not in "-0123456789": return False
    for i in x2:
        if i not in "0123456789": return False
    return True

def calculation(a, b, fg):
    if len(a) + len(b) < 4: return False
    if not(check(a) and check(b)): return False
    x1 = Fraction(int(a[0]), int(a[1]))
    x2 = Fraction(int(b[0]), int(b[1]))
    result = eval(f"x1 {fg} x2")
    return result.numerator, result.denominator

def calculation2():
    a = [entry_1.get(), entry_2.get()]
    b = [entry_3.get(), entry_4.get()]
    fg = selected.get()
    result = calculation(a, b, fg)
    if result:
        label_3.place(x=260, y=55)
        label_4.config(text=f"{result[0]}")
        label_5.config(text=f"{result[1]}")
        label_6.config(text=f"{'_'*max(len(str(result[1])),len(str(result[0])))}")
        label_4.place(x=280, y=40)
        label_5.place(x=280, y=80)
        label_6.place(x=280, y=55)
    else:
        clear()

def clear():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)
    label_3.place_forget()
    label_4.place_forget()
    label_5.place_forget()
    label_6.place_forget()
    selected.set(options[0])

root = tk.Tk()
root.geometry("500x300")
root.resizable(width=False,height=False)

options = ["+", "-", "*", "/"]

label_1 = tk.Label(root,text="_____________")
label_2 = tk.Label(root,text="_____________")
label_3 = tk.Label(root,text="=")
label_4 = tk.Label(root,text="")
label_5 = tk.Label(root,text="")
label_6 = tk.Label(root,text="")

entry_1 = tk.Entry(root, width=10)
entry_2 = tk.Entry(root, width=10)
entry_3 = tk.Entry(root, width=10)
entry_4 = tk.Entry(root, width=10)

selected = tk.StringVar()
selected.set(options[0])
lst_1 = tk.OptionMenu(root, selected, *options)

button_1 = tk.Button(root, text="Вычислить", width=20, command=calculation2)

button_1.place(x=180, y=260)
label_1.place(x=35, y=50)
entry_1.place(x=40, y=40)
entry_2.place(x=40, y=75)
lst_1.place(x=120, y=50)
label_2.place(x=185, y=50)
entry_3.place(x=190, y=40)
entry_4.place(x=190, y=75)

root.mainloop()