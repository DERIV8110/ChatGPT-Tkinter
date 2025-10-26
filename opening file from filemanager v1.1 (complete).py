from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
root.title("VapidTech gallery v1.1")
root.iconbitmap('C:/python images/feather.ico')                         # root.iconbitmab() --> icon of the app  

file_path = filedialog.askopenfilename(initialdir="C:/python images",title="select a file",filetypes=(("png files","*.png"),("all files","*.*")))

my_img =ImageTk.PhotoImage(Image.open(file_path))
                                                                        # imagetk.photoimage(image.open()) -->shows image from location provided
my_label=Label(image=my_img).grid(row=0,column=0)
button_exit = Button(root,text="Close",command=root.quit,font=("Arial",10),pady=10,width=20,bg="blue",fg="white").grid(row=1,column=0)

root.mainloop()