from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("VapidTech gallery v1.1")

root.iconbitmap('C:/')

my_img =ImageTk.PhotoImage(Image.open("C:/python images/img1.jpg"))

my_label=Label(image=my_img)

my_label.pack()

root.mainloop()