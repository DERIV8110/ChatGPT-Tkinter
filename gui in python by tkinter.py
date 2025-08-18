import tkinter as tk

def say_hello():
    label.config(text="Hello, " + entry.get())

root = tk.Tk()
root.title("Simple UI")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Click me", command=say_hello)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
