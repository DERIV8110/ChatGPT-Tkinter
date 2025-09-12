from tkinter import *
root=Tk()

def myclick():    #text appears after clicking button
       mylabel=Label(root,text="you have clicked the button")  #bg,fg can also be added
       mylabel.pack()
mybutton=Button(root,text="click here!",bg="black",fg="white",command=myclick)
                                         #command shows mylabel after clicking button
                                         #status=DISABLED disables the button
mybutton.pack()
root.mainloop()

