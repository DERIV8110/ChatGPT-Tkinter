from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root= Tk()
root.title("Login into vapid comms")
root.iconbitmap('C:/python images/vapidTech.ico')

text1=Label(root,text="Login to Vapid Comms?",font="Helvetica, 24").pack()

my_img1 =ImageTk.PhotoImage(Image.open("C:/python images/vapidTechLOGO.jpg"))
mlabel1=Label(image=my_img1).pack()
def pagetwo():
       top = Toplevel()
       top.geometry("1000x560")
       top.title("Vapid comms.")

       mlabel=Label(top, text="Enter Username",font="Helvetica, 24")     #this is a new windows so evey argu. will be top not root.
       mlabel.pack(pady=50,padx=50)

       e=Entry(top,width=50,bg="black",fg="white")                       #this is a new window so evey argu. will be top not root.
       e.insert(0,"ex: abhilashray45")
       e.pack(ipady=10)


       b2=Button(top,text="Continue")                                    #this is a new window so evey argu. will be top not root.
       b2.pack(padx=50,pady=30) 


b1=Button(root,text="Continue",command=pagetwo)
b1.pack(padx=50,pady=30)
root.geometry("1000x560")
root.mainloop()