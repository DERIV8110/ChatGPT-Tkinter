from tkinter import *
root=Tk()

e=Entry(root,width=50,bg="black",fg="white")   #makes boxes
e.pack()

e.insert(0,"enter your name here")  #pre-written text in box
def myclick():    #text appears after clicking button
       mylabel=Label(root,text=e.get())  #bg,fg can also be added
                                         #e.get() calls e function 
       mylabel.pack()
mybutton=Button(root,text="enter your stock name",command=myclick)
                                         #command shows mylabel after clicking button
                                         #status=DISABLED disables the button
mybutton.pack()
root.mainloop()