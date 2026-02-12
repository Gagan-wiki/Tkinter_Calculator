import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="black")
entry = tk.Entry(
    root,
    font=("Times New Roman", 20),
    bg="grey",
    fg="white",
    bd=10,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

buttons = [
    "1","2","3","+",
    "4","5","6","-",
    "7","8","9","*",
    ".","0","/","=",
    "C"
]

r = 1
c = 0

for b in buttons:
    if b == "=":
        cmd = calc
    elif b == "C":
        cmd = clear
    else:
        cmd = lambda x=b: click(x)

    tk.Button(
        root,
        text=b,
        font=("Times New Roman", 15),
        width=5,
        height=2,
        bg="grey" if b not in "+-*/=" else "orange",
        fg="white",
        command=cmd
    ).grid(row=r, column=c, padx=5, pady=5)

    c += 1
    if c == 4:
        r += 1
        c = 0

root.mainloop()

