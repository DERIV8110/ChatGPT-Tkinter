from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root= Tk()
root.title("Login into vapid comms")
root.iconbitmap('C:/python images/vapidTech.ico')

text1=Label(root,text="Login to Vapid Comms?",font="Calibri, 20").pack()

my_img1 =ImageTk.PhotoImage(Image.open("C:/python images/vapidTechLOGO.jpg"))
mlabel1=Label(image=my_img1).pack()
def pagetwo():
       top = Toplevel()
       top.geometry("700x450")
       top.title("Vapid comms.")

       mlabel=Label(top, text="Enter Username",font="Calibri, 20")                                     #this is a new windows so evey argu. will be top not root.
       mlabel.pack(pady=50,padx=50)

       e=Entry(top,width=50)                                          
       e.insert(0,"ex: abhilashray45") 
       e.pack(ipady=10)                                                                                # ipady= --> increases height of the box

       def res():
              res = messagebox.askokcancel(message="Are you sure?")
              if res==1:
                     if e.get()=="rishav":
                            top = Toplevel()
                            top.geometry("700x450")                                                   # .geometry --> set window size in pixels
                            top.title("Vapid comms.")

                            mlabel2=Label(top, text="username found!",font="Calibri, 20")              #new window--> do not use root--> use top 
                            mlabel2.pack(pady=50,padx=50)
                            f=Entry(top,width=50)                                                      #new window--> do not use root--> use top
                            f.insert(0,"enter password...") 
                            f.pack(ipady=10)

                            def pagethree():
                                   if f.get()=="abcx":
                                          messagebox.showinfo(message="logged in successfully!")
                                   else:
                                          messagebox.showerror(message="incorrect password!")

                            b4=Button(top,text="Continue",command=pagethree)                           # defined function -->above button whose command is defined function
                            b4.pack(padx=50,pady=30)

                     else:
                            top = Toplevel()
                            top.geometry("700x450")                                                   # .geometry --> set window size in pixels
                            top.title("Vapid comms.")

                            messagebox.showerror(message="incorrect username!")
                            
                            
              else:
                     top.destroy()

       b2=Button(top,text="Continue",command=res)                                                      # defined function -->above button whose command is defined function
       b2.pack(padx=50,pady=30)



b1=Button(root,text="Continue",command=pagetwo)                                                        # defined function -->above button whose command is defined function
b1.pack(padx=50,pady=30)
root.geometry("700x450")                                                                               # .geometry --> set window size in pixels
root.mainloop()