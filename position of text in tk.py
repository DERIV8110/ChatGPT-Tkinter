from tkinter import *
root=Tk()
mylabel1=Label(root,text="Hello!!")
mylabel2=Label(root,text="my name is abhilash ray.")

#below changes position of text in tkinter window
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=1)

root.mainloop()