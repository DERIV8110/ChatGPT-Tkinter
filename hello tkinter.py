from tkinter import *

root=Tk()

mylabel=Label(root,text="hello tkinter!")
#label prints desired text in gui
mylabel.pack()
#mylabel is a package packed by mylabel.pack
root.mainloop()
#add this to every code to keep it running (MUST!)
