from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root= Tk()
root.title("Login into vapid comms")
root.iconbitmap('C:/python images/vapidTech.ico')

def popup():
       global res
       mlabel3=Label(root, text="enter password below")
       mlabel3.pack()
       res = messagebox.askokcancel()

if messagebox.askokcancel()==1:
              e=Entry(root,width=50,bg="black",fg="white")
              e.insert(0,"enter username")              
              e.pack()
              res = messagebox.askokcancel()
              if e.get()=="rishav":
                  top = Toplevel()
                  top.geometry("300x200")
                  top.title("Vapid comms.")

                  mlabel=Label(top, text="enter password below")
                  mlabel.pack(pady=50,padx=50)
              else:
                     top2 = Toplevel()
                     top2.geometry("300x200")
                     top2.title("Vapid comms.")

                     mlabel2=Label(top2, text="wrong password try again!")
                     mlabel2.pack(pady=50,padx=50)




Button(root,text="Login",command=popup).pack()