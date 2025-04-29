import tkinter as tk
import math

def press(num):
    entry.insert(tk.END, str(num))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        # Use eval with math functions available in the global namespace
        expression = entry.get()
        # Replace '^' with '**' for exponentiation
        expression = expression.replace('^', '**')
        # Handle square operation by replacing x² with **2
        expression = expression.replace('x²', '**2')
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=30, font=('Arial', 18), bd=4, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=6)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sin',1,4), ('cos',1,5),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('tan',2,4), ('log',2,5),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('x²',3,4), ('√',3,5),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3), ('(',4,4), (')',4,5),
    ('C',5,0)
]

for (text, r, c) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, command=calculate).grid(row=r, column=c)
    elif text == 'C':
        tk.Button(root, text=text, width=32, height=2, command=clear).grid(row=r, column=c, columnspan=6)
    elif text == '√':
        def sqrt_press():
            try:
                value = float(entry.get())
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(math.sqrt(value)))
            except:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")
        tk.Button(root, text=text, width=5, height=2, command=sqrt_press).grid(row=r, column=c)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t + '(') if t in ['sin', 'cos', 'tan', 'log'] else press(t)).grid(row=r, column=c)

root.mainloop()
