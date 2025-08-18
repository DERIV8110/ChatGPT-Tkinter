import tkinter as tk

# Function to update expression in the entry field
def press(key):
    entry_var.set(entry_var.get() + str(key))

# Function to evaluate the final expression
def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except Exception:
        entry_var.set("Error")

# Function to clear the entire entry field
def clear_all():
    entry_var.set("")

# Function to clear last character (like backspace)
def clear_last():
    entry_var.set(entry_var.get()[:-1])

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x450")

entry_var = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 18), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        action = calculate
    else:
        action = lambda x=text: press(x)
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)

# Clear last (C) button
tk.Button(root, text='C', width=10, height=2, font=('Arial', 14),
          command=clear_last).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Clear all (AC) button
tk.Button(root, text='AC', width=10, height=2, font=('Arial', 14),
          command=clear_all).grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
